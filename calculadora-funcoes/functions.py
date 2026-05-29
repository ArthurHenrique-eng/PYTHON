import math

class FunctionError(Exception):
    """Exceção para erros em cálculos de funções"""
    pass


class FirstDegreeFunction:
    """Função do primeiro grau: f(x) = ax + b"""

    def __init__(self, a, b):
        if a == 0:
            raise FunctionError("Coeficiente 'a' não pode ser zero para função do primeiro grau")
        self.a = a
        self.b = b

    def evaluate(self, x):
        """Calcula f(x) = ax + b"""
        return self.a * x + self.b

    def root(self):
        """Encontra a raiz: f(x) = 0 => x = -b/a"""
        return -self.b / self.a

    def slope(self):
        """Retorna o coeficiente angular (inclinação)"""
        return self.a

    def y_intercept(self):
        """Retorna o intercepto y (valor quando x=0)"""
        return self.b

    def is_increasing(self):
        """Verifica se a função é crescente ou decrescente"""
        return self.a > 0

    def __str__(self):
        sign = "+" if self.b >= 0 else "-"
        return f"f(x) = {self.a}x {sign} {abs(self.b)}"


class SecondDegreeFunction:
    """Função do segundo grau: f(x) = ax² + bx + c"""

    def __init__(self, a, b, c):
        if a == 0:
            raise FunctionError("Coeficiente 'a' não pode ser zero para função do segundo grau")
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x):
        """Calcula f(x) = ax² + bx + c"""
        return self.a * (x ** 2) + self.b * x + self.c

    def delta(self):
        """Calcula o discriminante Δ = b² - 4ac"""
        return (self.b ** 2) - (4 * self.a * self.c)

    def roots(self):
        """Encontra as raízes usando Baskara: x = (-b ± √Δ) / 2a"""
        delta = self.delta()

        if delta < 0:
            return None, None  # Sem raízes reais
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return x, x  # Raiz dupla
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-self.b + sqrt_delta) / (2 * self.a)
            x2 = (-self.b - sqrt_delta) / (2 * self.a)
            return x1, x2

    def vertex(self):
        """Calcula o vértice da parábola: V = (-b/2a, f(-b/2a))"""
        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.evaluate(x_vertex)
        return x_vertex, y_vertex

    def axis_of_symmetry(self):
        """Retorna o eixo de simetria: x = -b/2a"""
        return -self.b / (2 * self.a)

    def is_concave_up(self):
        """Verifica se a parábola tem concavidade para cima (a > 0)"""
        return self.a > 0

    def minimum_value(self):
        """Retorna o valor mínimo se a > 0"""
        if not self.is_concave_up():
            return None
        _, y_min = self.vertex()
        return y_min

    def maximum_value(self):
        """Retorna o valor máximo se a < 0"""
        if self.is_concave_up():
            return None
        _, y_max = self.vertex()
        return y_max

    def root_count(self):
        """Retorna o número de raízes reais: 0, 1 ou 2"""
        delta = self.delta()
        if delta < 0:
            return 0
        elif delta == 0:
            return 1
        else:
            return 2

    def __str__(self):
        sign_b = "+" if self.b >= 0 else "-"
        sign_c = "+" if self.c >= 0 else "-"
        return f"f(x) = {self.a}x² {sign_b} {abs(self.b)}x {sign_c} {abs(self.c)}"


class FunctionAnalyzer:
    """Análise completa de funções"""

    @staticmethod
    def analyze_first_degree(a, b):
        """Retorna análise completa da função do primeiro grau"""
        func = FirstDegreeFunction(a, b)
        return {
            'function': str(func),
            'root': func.root(),
            'slope': func.slope(),
            'y_intercept': func.y_intercept(),
            'is_increasing': func.is_increasing(),
            'type': 'Função Linear'
        }

    @staticmethod
    def analyze_second_degree(a, b, c):
        """Retorna análise completa da função do segundo grau"""
        func = SecondDegreeFunction(a, b, c)
        x1, x2 = func.roots()

        return {
            'function': str(func),
            'delta': func.delta(),
            'roots': (x1, x2),
            'root_count': func.root_count(),
            'vertex': func.vertex(),
            'axis_of_symmetry': func.axis_of_symmetry(),
            'concave_up': func.is_concave_up(),
            'minimum': func.minimum_value(),
            'maximum': func.maximum_value(),
            'type': 'Função Quadrática'
        }
