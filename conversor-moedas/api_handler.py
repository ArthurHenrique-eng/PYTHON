import requests
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


class APIHandler:
    """Gerencia integração com APIs de câmbio em tempo real"""

    # APIs suportadas
    AVAILABLE_APIS = {
        'exchangerate': 'https://api.exchangerate-api.com/v4/latest',
        'fixer': 'https://api.fixer.io/latest',
        'openexchangerates': 'https://api.openexchangerates.org/latest'
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.timeout = 10
        self.cache_file = Path(__file__).parent / 'data' / 'cache.json'

    def fetch_rates_exchangerate_api(self, base: str = 'USD') -> Optional[Dict]:
        """
        Busca taxas da API exchangerate-api.com (gratuita).

        Args:
            base: Moeda base

        Returns:
            Dicionário com taxas ou None se falhar
        """
        try:
            url = f"{self.AVAILABLE_APIS['exchangerate']}/{base}"
            response = self.session.get(url)
            response.raise_for_status()

            data = response.json()
            return {
                'base': data.get('base', base),
                'rates': data.get('rates', {}),
                'timestamp': datetime.now().timestamp()
            }
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao conectar com exchangerate-api: {e}")
            return None

    def fetch_rates_fixer_io(self, api_key: str, base: str = 'EUR') -> Optional[Dict]:
        """
        Busca taxas da API fixer.io (requer chave de API).

        Args:
            api_key: Chave de API do fixer.io
            base: Moeda base

        Returns:
            Dicionário com taxas ou None se falhar
        """
        try:
            params = {'base': base, 'access_key': api_key}
            response = self.session.get(self.AVAILABLE_APIS['fixer'], params=params)
            response.raise_for_status()

            data = response.json()
            if not data.get('success', False):
                print(f"⚠️ Erro na resposta do Fixer.io: {data.get('error', {}).get('info', 'Desconhecido')}")
                return None

            return {
                'base': data.get('base', base),
                'rates': data.get('rates', {}),
                'timestamp': datetime.now().timestamp()
            }
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao conectar com fixer.io: {e}")
            return None

    def fetch_rates_openexchangerates(self, api_key: str, base: str = 'USD') -> Optional[Dict]:
        """
        Busca taxas da API openexchangerates.org (requer chave de API).

        Args:
            api_key: Chave de API do openexchangerates
            base: Moeda base

        Returns:
            Dicionário com taxas ou None se falhar
        """
        try:
            params = {'base': base, 'app_id': api_key}
            response = self.session.get(self.AVAILABLE_APIS['openexchangerates'], params=params)
            response.raise_for_status()

            data = response.json()
            return {
                'base': data.get('base', base),
                'rates': data.get('rates', {}),
                'timestamp': datetime.now().timestamp()
            }
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao conectar com openexchangerates: {e}")
            return None

    def save_to_cache(self, data: Dict) -> None:
        """Salva dados em cache local"""
        try:
            cache_data = {
                'timestamp': data.get('timestamp', datetime.now().timestamp()),
                'base': data.get('base', 'USD'),
                'rates': data.get('rates', {})
            }

            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2)
        except Exception as e:
            print(f"⚠️ Erro ao salvar cache: {e}")

    def load_from_cache(self) -> Optional[Dict]:
        """Carrega dados do cache local"""
        try:
            if self.cache_file.exists():
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️ Erro ao carregar cache: {e}")

        return None

    def update_with_cache_fallback(self, api_key: str = None) -> Optional[Dict]:
        """
        Tenta atualizar com API, usa cache se falhar.

        Args:
            api_key: Chave de API (opcional)

        Returns:
            Dicionário com taxas atualizado ou do cache
        """
        # Tenta API gratuita primeiro
        data = self.fetch_rates_exchangerate_api()

        # Se falhar e temos chave, tenta outras APIs
        if not data and api_key:
            data = self.fetch_rates_fixer_io(api_key)
            if not data:
                data = self.fetch_rates_openexchangerates(api_key)

        # Se API falhar, usa cache
        if not data:
            print("ℹ️ Usando dados em cache...")
            data = self.load_from_cache()

        # Se conseguiu dados via API, salva em cache
        if data:
            self.save_to_cache(data)

        return data
