#Variables globales 
result = 0
#Funciones
def run(n: int) -> int:
    # TODO
    global result
    #Variables locales
    result = str(n)
    result = (f"{n}{n*2}{n*3}") 
    return result

#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(result)