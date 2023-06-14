#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid Python list object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Python bytes object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *bytes = PyBytes_AsString(p);

    printf("[.] Bytes object info\n");
    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", bytes);

    printf("  first %ld bytes:", size + 1);
    if (size > 10)
        size = 10;

    for (Py_ssize_t i = 0; i <= size; ++i)
        printf(" %02hhx", bytes[i]);
    printf("\n");
}
