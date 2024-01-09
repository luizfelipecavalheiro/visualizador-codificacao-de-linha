# visualizador-codificacao-de-linha
- Sistema de visualização para os códigos de linha NRZ-I, NRZ-L, AMI, Pseudoternário, Manchester e Mancherter Diferencial

### Padrões:
- NRZ-L: RS-232
- NRZ-I: USB
- AMI: tronco digital T1 (ISDN primário 1544Mbps)
- Pseudoternário: interface ISDN básica (192kbps)
- Manchester: IEEE 802.3
- Manchester Diferencial: IEEE 802.5

### Modo de Uso:
- Execute o arquivo `main.py` em uma máquina que possua Python 3 instalado, ou então em algum compilador online que possua as bibliotecas `Tkinter` e `Matplotlib` (ambas já vem com a instalação padrão do Python, exceto distros Linux que necessitam a instalação destas bibliotecas separadamente).
- Após a execução surgirá a tela principal que possui alguns `widgets`, são eles:
  - Uma caixa de combinação, também conhecida como `combobox` contendo os padrões citados acima;
  - Uma caixa de texto que aceita a entrada somente de dígitos binários;
  - Um botão `Gerar Gráfico` que levará a tela contendo a visualização do padrão escolhido correspondente a entrada digitada;


- Selecione um padrão, digite uma entrada binária e clique no botão `Gerar Gráfico`:
  - Após, será direcionado a uma nova tela contendo:
    -  o nome do padrão;
    -  a entrada binária digitada:
    -  o gráfico correspondente;
    -  o botão `Voltar`, caso deseje voltar para a tela principal para escolher outro padrão ou outra entrada binária.
