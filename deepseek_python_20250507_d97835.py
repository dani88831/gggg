import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# Dados
anos = ['2021', '2022', '2023']
tratamentos = ['Controle', 'N80', 'GM_2M', 'GM_2.5M', 'GM_3M']
rend_milho = [
    [7.20, 8.30, 8.50, 8.60, 8.75],  # 2021
    [1.61, 2.40, 3.70, 3.75, 4.10],  # 2022
    [11.80, 11.85, 11.95, 12.00, 12.11]  # 2023
]
prec_outubro = [197.3, 1.7, 15.4]
biomass_media = [12.27, 0.76, 3.07]
cores = ['#FF6B6B', '#4D8AC8', '#2ECC71', '#27AE60', '#229954']

# Criar PDF
with PdfPages("Relatorio_Adubacao_Verde_Graficos.pdf") as pdf:
    
    # Gráfico 1: Rendimento do milho
    fig1, ax1 = plt.subplots(figsize=(12, 7))
    x = np.arange(len(anos))
    width = 0.15
    for i in range(len(tratamentos)):
        valores = [rend_milho[ano][i] for ano in range(len(anos))]
        ax1.bar(x + i * width, valores, width, label=tratamentos[i], color=cores[i])
        for j, v in enumerate(valores):
            ax1.text(x[j] + i * width, v + 0.1, f'{v:.1f}', ha='center', color='black', fontsize=8)
    
    ax1.set_title('Rendimento de Milho por Tratamento e Ano', fontsize=14, pad=20)
    ax1.set_xlabel('Ano', fontsize=12)
    ax1.set_ylabel('Rendimento (t/ha)', fontsize=12)
    ax1.set_xticks(x + 2 * width)
    ax1.set_xticklabels(anos)
    ax1.legend(title='Tratamento', bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    pdf.savefig(fig1)
    plt.close(fig1)
    
    # Gráfico 2: Precipitação vs. Biomassa
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.scatter(prec_outubro, biomass_media, color='green', s=100, edgecolor='black', zorder=3)
    for i, year in enumerate(['2020', '2021', '2022']):
        ax2.annotate(year, (prec_outubro[i], biomass_media[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    
    # Linha de tendência
    z = np.polyfit(prec_outubro, biomass_media, 1)
    p = np.poly1d(z)
    ax2.plot(prec_outubro, p(prec_outubro), "r--", label='Tendência')
    
    # R²
    r2 = np.corrcoef(prec_outubro, biomass_media)[0, 1]**2
    ax2.text(100, 10, f'R² = {r2:.2f}', fontsize=12, color='red')
    
    ax2.set_title('Correlação entre Precipitação em Outubro e Biomassa de Ervilhaca', fontsize=14, pad=20)
    ax2.set_xlabel('Precipitação em Outubro (mm)', fontsize=12)
    ax2.set_ylabel('Biomassa Média (t/ha)', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend()
    plt.tight_layout()
    pdf.savefig(fig2)
    plt.close(fig2)

print("✅ PDF gerado: Relatorio_Adubacao_Verde_Graficos.pdf")