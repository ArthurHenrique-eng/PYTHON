import matplotlib.pyplot as plt
import numpy as np
from .functions import FirstDegreeFunction, SecondDegreeFunction


class FunctionGrapher:
    """Cria gráficos de funções matemáticas"""

    @staticmethod
    def plot_first_degree(a, b, x_range=None, title=None):
        """Plota gráfico de função do primeiro grau"""
        func = FirstDegreeFunction(a, b)

        if x_range is None:
            x_range = (-10, 10)

        x = np.linspace(x_range[0], x_range[1], 100)
        y = [func.evaluate(xi) for xi in x]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=str(func))

        # Marca a raiz
        root = func.root()
        plt.plot(root, 0, 'ro', markersize=8, label=f'Raiz: x = {root:.2f}')

        # Marca o intercepto y
        plt.plot(0, func.y_intercept(), 'go', markersize=8, label=f'Intercepto Y: {func.y_intercept():.2f}')

        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(title or str(func), fontsize=14)
        plt.legend(fontsize=10)

        return plt

    @staticmethod
    def plot_second_degree(a, b, c, x_range=None, title=None):
        """Plota gráfico de função do segundo grau"""
        func = SecondDegreeFunction(a, b, c)

        if x_range is None:
            x_range = (-10, 10)

        x = np.linspace(x_range[0], x_range[1], 200)
        y = [func.evaluate(xi) for xi in x]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=str(func))

        # Marca o vértice
        vx, vy = func.vertex()
        plt.plot(vx, vy, 'mo', markersize=10, label=f'Vértice: ({vx:.2f}, {vy:.2f})')

        # Marca as raízes se existirem
        x1, x2 = func.roots()
        if x1 is not None and x2 is not None:
            if x1 == x2:
                plt.plot(x1, 0, 'ro', markersize=8, label=f'Raiz dupla: x = {x1:.2f}')
            else:
                plt.plot(x1, 0, 'ro', markersize=8, label=f'Raízes: x₁ = {x1:.2f}, x₂ = {x2:.2f}')
                plt.plot(x2, 0, 'ro', markersize=8)

        # Eixo de simetria
        axis = func.axis_of_symmetry()
        plt.axvline(x=axis, color='r', linestyle='--', alpha=0.5, label=f'Eixo de simetria: x = {axis:.2f}')

        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(title or str(func), fontsize=14)
        plt.legend(fontsize=10)

        return plt

    @staticmethod
    def plot_multiple_functions(functions, labels, x_range=None, title="Múltiplas Funções"):
        """Plota múltiplas funções no mesmo gráfico"""
        if x_range is None:
            x_range = (-10, 10)

        plt.figure(figsize=(12, 7))
        colors = ['b', 'r', 'g', 'm', 'c', 'orange']

        for i, (func, label) in enumerate(zip(functions, labels)):
            x = np.linspace(x_range[0], x_range[1], 200)
            y = [func(xi) for xi in x]
            plt.plot(x, y, color=colors[i % len(colors)], linewidth=2, label=label)

        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(title, fontsize=14)
        plt.legend(fontsize=10)

        return plt
