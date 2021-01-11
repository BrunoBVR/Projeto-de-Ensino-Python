import numpy as np
import matplotlib.pyplot as plt

# # Vamos começar com a caminho aleatório 1D


# # Sempre definam a semente para conseguir reproduzir os resultados
# np.random.seed(5)

# # Vamos começar o passeio aleatório na origem
# x = 0

# # Definimos o número de passos que queremos analisar
# N = 10000

# # Aqui, o passo é definido como um passo à direita ou à esquerda
# # A PROBABILIDADE DE DAR UM PASSO À DIREITA É IGUAL À DE DAR UM PASSO PARA A ESQUERDA!

# ## Passo à direita  x += 1
# ## Passo à esquerda x -= 1

# # Loop para "dar N passos"
# for i in np.arange(N):
# 	r = np.random.rand()		# Gera um número aleatório no intervalo [0,1)

# 	# Passo à direita
# 	if r < 0.5:
# 		x += 1
# 	# Passo à esquerda
# 	else:
# 		x -= 1

# # Vamos ver onde o "caminhador" terminou
# # print(x)

# # Se fizermos o caminho várias vezes, podemos salvar a posição
# # final em cada passeio. Faremos isso em uma lista
# x_final = np.array([])

# # Vamos definir diferentes passeios com diferentes sementes

# # Definimos quantos passeios vamos fazer
# N_passeios = 1000

# # NOTEM: para cada um dos N_passeios, daremos N passos

# # Já percebam que precisaremos de dois loops:
# ### Um para dar N passos
# ### Outro para fazer N_passeios

# # Primeiro loop
# for i in np.arange(N_passeios):
# 	# np.random.seed(i)
# 	x = 0
# 	# Loop para cada passeio
# 	for i in np.arange(N):
# 		r = np.random.rand()		# Gera um número aleatório no intervalo [0,1)

# 		# Passo à direita
# 		if r < 0.5:
# 			x += 1
# 		# Passo à esquerda
# 		else:
# 			x-= 1

# 	# Salvar o x final na lista x_final
# 	x_final = np.append(x_final, x)


# print("="*20)
# print(x_final.mean())
# print("="*20)

# plt.plot(x_final)
# plt.show()

# plt.hist(x_final)
# plt.xlabel("Posição Final")
# plt.ylabel("Contagem")
# plt.grid()
# plt.show()



#### TUDO COMENTADO ACIMA
funcional = False
if funcional:
	# Podemos deixar tudo isso bem mais limpo.
	# O Loop interno, por exemplo, pode ser transformado em função:

	# Definir função para dar N passos:
	def passos(N):
		'''
		Função que retorna a posição de um passeio aleatório
		1D após N passos iniciado na origem.
		'''
		x = 0
		for i in np.arange(N):
			r = np.random.rand()

			# Passo à direita
			if r < 0.5:
				x += 1
			# Passo à esquerda
			else:
				x -= 1
		return x

	# Definir função para plotar resultado final
	def plot_hist(x):
		plt.hist(x_final, color='g', alpha=0.5, ec='k')
		plt.xlabel("Posição Final")
		plt.ylabel("Contagem")

		plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)

		plt.show()

	# Função para plotar posição final de cada passeio na linha
	def plot_linha(x, N_passeios):
		plt.scatter(x, np.ones(int(N_passeios)), s = 0.5)
		plt.xlabel("Posição")
		plt.show()		

	# Número de passos em cada passeio
	N = 1e3
	# Número de passeios
	N_passeios = 1e3
	# Fixar a semente
	np.random.seed(42)
	# Define vetor com as posições finais
	x_final = np.array([])

	# Primeiro loop
	for i in np.arange(N_passeios):

		# Salvar o x final na lista x_final
		x_final = np.append(x_final, passos(N))

	# plt.plot(x_final)
	# plt.show()

	plot_hist(x_final)

	plot_linha(x_final, N_passeios)


####################################
# Passeio aleatório 2D
####################################

np.random.seed(42)

# Agora o passeio é feito em um plano
# Cada passo tem tamanho 1 (módulo 1)
# Cada passo pode ser em qualquer direção.
d_2D = True
if d_2D:
	def passos_2D(N, plota = False):
		# Comecemos da origem (agora precisamos de um vetor posição 2D)
		X = 0.0
		Y = 0.0

		if plota:
			# Definir vetor com histórico das posições
			x_passeio = np.array([X])
			y_passeio = np.array([Y])

		for i in np.arange(N):
			ang = np.random.rand()*2*np.pi
			X += np.cos(ang)
			Y += np.sin(ang)

			if plota:

				x_passeio = np.append(x_passeio, X)

				y_passeio = np.append(y_passeio, Y)

		if plota:
			plt.plot(x_passeio, y_passeio, lw=0.3, color='r')
			plt.show()

		return X, Y


	# Definir número de passos
	N = 1000

	# Visualizando um único passeio
	X, Y = passos_2D(N, plota=True)


	# Definir quantos passeios vamos fazer:
	N_passeios = 100

	X_final = np.array([])
	Y_final = np.array([])

	# Loop para diferentes passeios
	for i in np.arange(N_passeios):
		X, Y = passos_2D(N)
		X_final = np.append(X_final, X)
		Y_final = np.append(Y_final, Y)

	plt.scatter(X_final, Y_final, s = 0.3, c = 'r')
	plt.show()

	# plt.hist2d(X_final, Y_final, bins=100)
	# plt.show()