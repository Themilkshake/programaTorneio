 
import random
 
 
class Jogador:
   def __init__(self, name, fake):
       self.name = name;
       self.ocupado = 0;
       self.wins = 0.0;
       self.derrotas = 0;
       self.score = 0;
       self.partidas = 0;
       self.empates = 0;
       self.winPorc = 0.0;
       self.lastAdvAdv = [];
       self.fake = fake;
 
def findOponent(jogadores, indexComp, total):
   terminou = True
   empates = []
   empates2 = []
 
   #primeiro por score, depois media de vitorias dos oponentes, depois media de vitorias dos oponentes dos oponentes
   scoreDif = 1000
   maiorMed = 0.0
   maiorMedOp = 0.0
 
   indexRet = 0
   score = jogadores[indexComp].score
   for i in range(0, total):
       if(i != indexComp and jogadores[i].ocupado == 0 and i not in jogadores[indexComp].lastAdvAdv):
           atualScoreDif = abs(score - jogadores[i].score)
           if(atualScoreDif < scoreDif):
               scoreDif = atualScoreDif
               indexRet = i
  
 
   empates.append(indexRet)
   #testo se tem scores iguais do que deve ser retornado
   for i in range(0, total):
       if(i != indexRet and i not in jogadores[indexComp].lastAdvAdv and jogadores[i].ocupado == 0):
           if(jogadores[i].score == jogadores[indexRet].score):
               terminou = False
               empates.append(i)
 
  
   if(terminou):
       return indexRet
  
   terminou = True
   ## agora por media de vitorias
   for i in empates:
       if(maiorMed < jogadores[i].winPorc):
           maiorMed = jogadores[i].winPorc
           indexRet = i
   ## checando se acabou mesmo
   empates2.append(indexRet)
   for i in empates:
       if(maiorMed == jogadores[i].winPorc and i != indexRet):
           terminou = False
           empates2.append(i)
 
   if(terminou):
       return indexRet
 
   ### por ultimo por media dos oponentes
 
   for i in empates2:
       total = 0
       for j in jogadores[i].lastAdvAdv:
           total += jogadores[j].winPorc
      
       if total > maiorMedOp:
           indexRet = i
           maiorMedOp = total
  
   return indexRet
 
def resolveVitoria(jogadores, total):
   terminou = True
   empates = []
   empates2 = []
   indexFinais = []
 
   #primeiro por score, depois media de vitorias dos oponentes, depois media de vitorias dos oponentes dos oponentes
   scoreMax = 0
   maiorMed = 0.0
   maiorMedOp = 0.0
 
   indexRet = 0
   for i in range(0, total):
       if(jogadores[i].score > scoreMax):
           scoreMax = jogadores[i].score
           indexRet = i
 
   empates.append(indexRet)
   #testo se tem scores iguais do que deve ser retornado
   for i in range(0, total):
       if(jogadores[i].score == jogadores[indexRet].score and i != indexRet):
           terminou = False
           empates.append(i)
 
  
   if(terminou):
       print("Vitoria do " + jogadores[indexRet].name + "!" )
       return
  
   terminou = True
   ## agora por media de vitorias
   for i in empates:
       if(maiorMed < jogadores[i].winPorc):
           maiorMed = jogadores[i].winPorc
           indexRet = i
   ## checando se acabou mesmo
   empates2.append(indexRet)
   for i in empates:
       if(maiorMed == jogadores[i].winPorc and i != indexRet):
           terminou = False
           empates2.append(i)
 
   if(terminou):
       print("Vitoria do " + jogadores[indexRet].name + "!")
       return
 
   ### por ultimo por media dos oponentes
   terminou = True
   for i in empates2:
       total = 0
       for j in jogadores[i].lastAdvAdv:
           total += jogadores[j].winPorc
      
       if total > maiorMedOp:
           indexRet = i
           maiorMedOp = total
  
 
   for i in empates2:
       total = 0
       for j in jogadores[i].lastAdvAdv:
           total += jogadores[j].winPorc
      
       if total == maiorMedOp and i != indexRet:
           terminou = False
           indexFinais.append(i)
  
   if(terminou):
       print("Vitoria do " + jogadores[indexRet].name + "!")
       return
  
   print("Empate entre:")
   for i in indexFinais:
       print(jogadores[i].name)
 
 
 
def resolveNaoAleatorio(jogadores, totalPessoas, rodadas):
   embates = int(totalPessoas/2)
   vezes = 0
   comparePos = -1
   combates = []
 
   # calculando os combates
   while(vezes < embates):
       comparePos += 1;
       if(jogadores[comparePos].ocupado == 0):
           vezes += 1;
           jogadores[comparePos].ocupado = 1
           index = findOponent(jogadores, comparePos, totalPessoas) # testa um index aleatorio
           jogadores[index].ocupado = 1;
           combates.append((comparePos, index))
           jogadores[index].partidas += 1
           jogadores[comparePos].partidas += 1
           print(str(vezes) + " duelo entre " + jogadores[comparePos].name + " e " + jogadores[index].name)
 
   # calculando os resultados
   for i in range(0, embates):
       nome1 = jogadores[combates[i][0]].name
       nome2 = jogadores[combates[i][1]].name
 
       # ez win
       if(nome1 == "Bye" or nome2 == "Bye"):
           if(nome1 == "Bye"):
               jogadores[combates[i][1]].wins += 1
               jogadores[combates[i][1]].score += 3
 
               jogadores[combates[i][0]].derrotas += 1
 
           else:
               jogadores[combates[i][0]].wins += 1
               jogadores[combates[i][0]].score += 3
 
               jogadores[combates[i][1]].derrotas += 1
 
       else:
           print("Digite o nome do vencedor do " + str(i+1) + " duelo (caso empate digite Bye):")
           nomeAtual = input()
           entrou = False
           if(nomeAtual == jogadores[combates[i][0]].name):
               entrou = True
 
               # ganhou
               jogadores[combates[i][0]].wins += 1
               jogadores[combates[i][0]].score += 3
               # perdeu
               jogadores[combates[i][1]].derrotas += 1
              
           elif nomeAtual == jogadores[combates[i][1]].name:
               entrou = True
 
               # ganhou
               jogadores[combates[i][1]].wins += 1
               jogadores[combates[i][1]].score += 3
               # perdeu
               jogadores[combates[i][0]].derrotas += 1
 
           if(not entrou):
               #empate
               jogadores[combates[i][0]].score += 1
               jogadores[combates[i][1]].score += 1
               jogadores[combates[i][0]].empates += 1
               jogadores[combates[i][1]].empates += 1
 
       jogadores[combates[i][0]].winPorc = jogadores[combates[i][0]].wins / jogadores[combates[i][0]].partidas
       jogadores[combates[i][1]].winPorc = jogadores[combates[i][1]].wins / jogadores[combates[i][1]].partidas
 
       jogadores[combates[i][1]].ocupado = 0
       jogadores[combates[i][0]].ocupado = 0
 
   rodadas -= 1
   if(rodadas > 0):
       resolveNaoAleatorio(jogadores, totalPessoas, rodadas)
   else:
       resolveVitoria(jogadores, totalPessoas)
 
def resolveAleatorio(jogadores, totalPessoas, rodadas):
   embates = int(totalPessoas/2)
   vezes = 0
   comparePos = -1
   combates = []
 
   while(vezes < embates):
       comparePos += 1;
       if(jogadores[comparePos].ocupado == 0):
           vezes += 1;
           jogadores[comparePos].ocupado = 1
           achou = False; # pra saber se achou o oponente
           while(not achou):
               index = random.randint(0, totalPessoas-1) # testa um index aleatorio
               if(jogadores[index].ocupado == 0):
                   jogadores[index].ocupado = 1
                   achou = True
                   combates.append((comparePos, index))
                   jogadores[index].partidas += 1
                   jogadores[index].lastAdvAdv.append(comparePos)
 
                   jogadores[comparePos].partidas += 1
                   jogadores[comparePos].lastAdvAdv.append(index)
 
                   print(str(vezes) + " duelo entre " + jogadores[comparePos].name + " e " + jogadores[index].name)
 
   # calculando os resultados
   for i in range(0, embates):
       nome1 = jogadores[combates[i][0]].name
       nome2 = jogadores[combates[i][1]].name
 
       # ez win
       if(nome1 == "Bye" or nome2 == "Bye"):
           if(nome1 == "Bye"):
               jogadores[combates[i][1]].wins += 1
               jogadores[combates[i][1]].score += 3
 
               jogadores[combates[i][0]].derrotas += 1
 
           else:
               jogadores[combates[i][0]].wins += 1
               jogadores[combates[i][0]].score += 3
 
               jogadores[combates[i][1]].derrotas += 1
       # normal
       else:
           print("Digite o nome do vencedor do " + str(i+1) + " duelo (caso empate digite Bye):")
           nomeAtual = input()
           entrou = False
           if(nomeAtual == jogadores[combates[i][0]].name):
               entrou = True
 
               # ganhou
               jogadores[combates[i][0]].wins += 1
               jogadores[combates[i][0]].score += 3
               # perdeu
               jogadores[combates[i][1]].derrotas += 1
              
           elif nomeAtual == jogadores[combates[i][1]].name:
               entrou = True
 
               # ganhou
               jogadores[combates[i][1]].wins += 1
               jogadores[combates[i][1]].score += 3
               # perdeu
               jogadores[combates[i][0]].derrotas += 1
 
           if(not entrou):
               #empate
               jogadores[combates[i][0]].score += 1
               jogadores[combates[i][1]].score += 1
               jogadores[combates[i][0]].empates += 1
               jogadores[combates[i][1]].empates += 1
 
       jogadores[combates[i][0]].winPorc = jogadores[combates[i][0]].wins / jogadores[combates[i][0]].partidas
       jogadores[combates[i][1]].winPorc = jogadores[combates[i][1]].wins / jogadores[combates[i][1]].partidas
 
       jogadores[combates[i][1]].ocupado = 0
       jogadores[combates[i][0]].ocupado = 0
 
   rodadas -= 1
   print("Rodada 2:")
   resolveNaoAleatorio(jogadores, totalPessoas, rodadas)
      
 
def resolveRodadas(total, power):
   if total <= 2**power:
       return power
   else :
       return resolveRodadas(total, power+1)
  
 
print("Digite o total de jogadores:");
total = int(input());
rodadas = resolveRodadas(total, 1);
 
jogadores = []
 
for i in range(0, total):
   print("Digite o nome do jogador " + str(i+1) + ":")
   atual = input()
   novo = Jogador(atual, 0)
   jogadores.append(novo)
  
if(total%2!=0):
   total += 1;
   novo = Jogador("Bye",1);
   jogadores.append(novo);
  
print("Rodada 1:")
resolveAleatorio(jogadores, total, rodadas);

print("Pressione qualquer botao para terminar...")
fim = input()
 
 
 
 


