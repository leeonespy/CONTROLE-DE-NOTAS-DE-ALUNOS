#modulo1
import csv, json

class Alunos: 
    def __init__(self, nome, M1, M2, M3):
        self.nome = nome
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        
        self.media_final = (self.M1 + self.M2 + self.M3) // 3
    
        if self.media_final >= 16:
            self.situacao = "Aprovado Com excelencia"
        elif self.media_final >= 10:
            self.situacao = "Aprovado"
        elif self.media_final == 8.5 or self.media_final == 9 or self.media_final == 9.5:
            self.situacao = "Aprovado Com recurso"
        elif self.media_final <= 8:
            self.situacao = "Reprovado"
        else:
            print("Erro no sistema de notas")
    
        self.dados = self.carregar_pauta()
        self.confirm()
        Turma().melhores_notas()
    
    def carregar_pauta(self):
        try:
            with open("mini_pauta.json", "r", encoding="utf-8") as arquivo:
                pauta = json.load(arquivo)
                return pauta
        except (FileNotFoundError, ValueError):
            return []
         
    def add_alunos(self):
            
        dados = {
            "Nome": self.nome,
            "Media1": self.M1,
            "Media2": self.M2,
            "Media3": self.M3,
            "Media_final": self.media_final,
            "Situação": self.situacao
            }
        
        self.dados.append(dados)     
        with open("mini_pauta.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dados, arquivo, indent=4)
            print("Dados adicionados com sucesso.")
            self.salvar(self.dados) 
        
    def salvar(self, dados):
        coluna = ["Nome", "Media1", "Media2", "Media3", "Media_final", "Situação"]
        with open("mini_pauta.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=coluna)
            f.seek(0, 2)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerows(dados)
        
    def confirm(self):
        
        with open("mini_pauta.json", "r", encoding="utf-8") as arquivo:
            pauta = json.load(arquivo)
            
            existe = False
        
            for lista in pauta:   
                if lista.get("Nome").strip().lower() == self.nome.strip().lower():
                    existe = True
                    break
                
            if existe:
               print("Nome já existe!")   
            else:
                self.add_alunos()
                

class Turma:
    def __init__(self):
        pass

    def melhores_notas(self, pauta="mini_pauta.json"):
        with open("mini_pauta.json", "r", encoding="utf-8") as arquivo:
            pauta = json.load(arquivo)

            melhor_nota = []
            for lista in pauta:   
                if lista["Media_final"] >= 15:
                   melhor_nota.append(lista)   
                else:
                    pass
            self.salvar(melhor_nota)    
            
    def salvar(self, dados):
        coluna = ["Nome", "Media1", "Media2", "Media3", "Media_final", "Situação"]
        with open("quadro_de_honra.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=coluna)
            f.seek(0, 2)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerows(dados)
    

    