from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def entrenar_evaluar_clasificador():
    # Cargar el conjunto de datos de Iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar el clasificador SVM
    clf = SVC()

    # Entrenar el clasificador
    clf.fit(X_train, y_train)

    # Predecir las etiquetas en el conjunto de prueba
    y_pred = clf.predict(X_test)

    # Calcular la precisión del clasificador
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

if __name__ == "__main__":
    accuracy = entrenar_evaluar_clasificador()
    print("Precisión del clasificador:", accuracy)
