palavra = ['c', 'a', 'u', 'ã', 'b', 'a', 'r', 'b', 'o', 's',]
v = ['a', 'e', 'i', 'o', 'u',]
palavrasqtd= len(palavra)
quantidadev= len(v)
quantidadec= palavrasqtd - quantidadev
result =str(quantidadec)
if palavra not in v:
    print ("A quantidade de Consoantes é:"  + result)