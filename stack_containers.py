from typing import Union


class Stack:
    def __init__(self, capacity: int) -> None:
        """Estructura de Pila para los contenedores

        Args:
            capacity (int): Tamaño maximo de la Pila
        """
        self.__list = []
        self.capacity = capacity

    def fill(self) -> None:
        """Llena la Pila de acuerdo a la capacidad establecida"""
        while self.size() < self.capacity:
            self.push(item=1)

    def unfill(self) -> None:
        """Vacia la pila"""
        while not self.is_empty():
            self.pop()

    def push(self, item: int) -> None:
        """Agrega un elemento a la Pila

        Args:
            item (int): elemento a agregar a la Pila
        """
        self.__list.append(item)

    def pop(self) -> Union[int, None]:
        """Elimina el elemento de arriba de la Pila

        Returns:
            Union[int, None]: Retorna el elemento que elimino
                              o no retorna nada si esta vacia
        """
        if self.__list == []:
            return print("Is Empty")
        else:
            return self.__list.pop()

    def peek(self) -> Union[int, None]:
        """Retorna el elemento de arriba de la Pila

        Returns:
            Union[int, None]: Retorna el valor del elemento de arriba
                              de la lista. O no retorna nada si la lista
                              está vacia
        """
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self) -> bool:
        """Determina si la Pila esta vacia

        Returns:
            bool: True si esta vacia, de lo contrario False
        """
        return self.__list == []

    def size(self) -> int:
        """Determina el tamaño de la PIla

        Returns:
            int: devuelve la longitud de la Pila
        """
        return len(self.__list)
