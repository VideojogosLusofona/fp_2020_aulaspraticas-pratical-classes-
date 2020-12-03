class Exemplo:

    def mensagem(self,a,b):
        self.a = a
        self.b = b
        
        if a == 4:
            raise ValueError("Eu nao gosto de 4")

        return self.a + self.b
      
            

ex = Exemplo().mensagem(2 ,3)

print(ex)