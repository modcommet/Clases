#Aqui defines las librerias que importaras
# Importar cobra y los casos de prueba
import cobra
import cobra.test

#Aqui escribes el codigo a ejecutar
def miFuncion():
    # Cargar el modelo de E coli
    model = cobra.test.create_test_model("ecoli")
    
    print "Running FVA=============="
    solution = model.optimize()
    model.summary(fva=1)

    print "Running Geometric FBA ============"
    geometric_fba_sol = cobra.flux_analysis.geometric_fba(model)
    geometric_fba_sol
    return 1

# Aqui se ejecuta el codigo
if __name__ == "__main__":
    miFuncion()
