novamente = 's'
while(novamente == 's'): # enquanto novamente for = 's', repita esse bloco abaixo.
#########################
	#####################################################################################################################
	c_humanas = float(raw_input("Entre sua nota em ciencias humanas e suas tecnologias:"))
	p_c_humanas =  float(raw_input("Entre o peso imposto para seu curso em ciencias humanas e suas tecnologias:"))
	c_naturais =  float(raw_input("Entre sua nota em ciencias da natureza e suas tecnologias:"))
	p_c_naturais =  float(raw_input("Entre o peso imposto para seu curso em ciencias da natureza e suas tecnologias:"))
	redacao =  float(raw_input("Entre sua nota em redacao:"))
	p_redacao =  float(raw_input("Entre o peso imposto para seu curso em redacao:"))
	linguagens =  float(raw_input("Entre sua nota em linguagens, codigos e suas tecnologias:"))
	p_linguagens =  float(raw_input("Entre o peso imposto para seu curso em linguagens, codigos e suas tecnologias:"))
	matematica =  float(raw_input("Entre sua nota em matematica e suas tecnologias:"))
	p_matematica =  float(raw_input("Entre o peso imposto para seu curso em matematica e suas tecnologias:"))
	p_total=p_c_humanas + p_c_naturais + p_redacao + p_linguagens + p_matematica # soma todos os pesos
	#####################################################################################################################
	########################################
	c_humanas = c_humanas * p_c_humanas # nota de humanas multiplicada pelo peso
	c_naturais = c_naturais * p_c_naturais # nota de naturais multiplicada pelo peso
	redacao = redacao * p_redacao # nota de redacao multiplicada pelo peso	
	linguagens = linguagens * p_linguagens # nota de linguagens multiplicada pelo peso
	matematica = matematica * p_matematica # nota de matematica multiplicada pelo peso
	########################################
	################################################################### 
	total = c_humanas + c_naturais + redacao + linguagens + matematica # soma tudo, provavelmente vai dar um valor bem alto...
	total = float(total / p_total) # divide o total das notas somadas pelo total dos pesos somados
	###################################################################
	########################################################
	print "Sua media no enem esta calculada em ",total
	print ""
	novamente = raw_input("Deseja tentar novamente?[s/n]") # auto-explicativo
	########################################################
	###########Sim, eu nao tenho nada melhor pra fazer. =)##
