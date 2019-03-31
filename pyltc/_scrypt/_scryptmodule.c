#include <Python.h>

#include "_scrypt.h"

static PyObject *scrypt_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyBytesObject *input;
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);
    scrypt_1024_1_1_256((char *)PyBytes_AsString((PyObject*) input), output);
    Py_DECREF(input);
    value = Py_BuildValue("y#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef module_methods[] = {
    { "getScryptHash", scrypt_getpowhash, METH_VARARGS, "Returns the proof of work hash using scrypt" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef _scryptmodule = {
    PyModuleDef_HEAD_INIT,
    "_scrypt",
    "...",
    -1,
    module_methods
};

PyMODINIT_FUNC PyInit__scrypt(void) {
    return PyModule_Create(&_scryptmodule);
}

