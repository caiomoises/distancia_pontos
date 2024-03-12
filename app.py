import streamlit as st
import matplotlib.pyplot as plt
import math

st.title("Calculadora de Distância entre Pontos")

x1 = st.number_input("Digite o valor de x1:")
y1 = st.number_input("Digite o valor de y1:")
x2 = st.number_input("Digite o valor de x2:")
y2 = st.number_input("Digite o valor de y2:")

if st.button("Calcular Distância"):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    st.write(f"A distância entre os dois pontos é: {distancia}")

    # exibir o passo a passo na interfase grafica
    st.title("Passo a passo:")
    st.write('x1 é o ponto inicial no eixo x\n')
    st.write('y1 é o ponto inicial no eixo y\n')
    st.write('x2 é o ponto final no eixo x\n')
    st.write('y2 é o ponto final no eixo y\n')
    st.latex(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')
    st.latex(r'd = \sqrt{('+str(x2)+' - '+str(x1)+')^2 + ('+str(y2)+' - '+str(y1)+')^2}')
    st.latex(r'd = \sqrt{('+str(x2 - x1)+')^2 + ('+str(y2 - y1)+')^2}')
    st.latex(r'd = \sqrt{'+str((x2 - x1)**2)+' + '+str((y2 - y1)**2)+'}')
    st.latex(r'd = \sqrt{'+str((x2 - x1)**2 + (y2 - y1)**2)+'}')
    st.latex(r'd = ' + str(distancia))

    # crie um grafico com grade em 3 dimensões para exibir os pontos e explicações sobre o calculo. crie um trascejado na cor preta, do ponto inicial ate o ponto final em x 
    plt.plot([x1, x2], [y1, y1], 'k--')
    plt.plot([x2, x2], [y1, y2], 'k--')
    plt.plot([x1, x2], [y1, y2], 'r-')
    plt.plot(x1, y1, 'ro')
    plt.plot(x2, y2, 'ro')
    plt.text(x1, y1, '(x1,y1)', fontsize=12, ha='left', va='bottom', rotation=0, color='blue', weight='bold', style='italic')
    plt.text(x2, y2, '(x2,y2)', fontsize=12, ha='right', va='bottom', rotation=0, color='blue', weight='bold', style='italic')

    plt.text((x1 + x2) / 2, y1 - 0.1, r'$\Delta X$', fontsize=12, ha='center', va='bottom', color='blue', weight='bold', style='italic')
    plt.text(x2 + 0.1, (y1 + y2) / 2, r'$\Delta Y$', fontsize=12, ha='left', va='center', color='blue', weight='bold', style='italic')
    
    plt.title('Distância entre dois pontos')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    st.pyplot(plt)
    if st.button("Limpar"):
        st.write("A tela foi limpa")
        plt.clf()
        plt.close()
        st.write("A tela foi limpa")