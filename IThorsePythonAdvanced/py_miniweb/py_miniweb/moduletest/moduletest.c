#include <Python.h>

/*
 * Implements an example function.
 */
PyDoc_STRVAR(moduletest_example_doc, "example(obj, number)\
\
Example function");

PyObject *moduletest_example(PyObject *self, PyObject *args, PyObject *kwargs) {
    /* Shared references that do not need Py_DECREF before returning. */
    PyObject *obj = NULL;
    int number = 0;

    /* Parse positional and keyword arguments */
    static char* keywords[] = { "obj", "number", NULL };
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "Oi", keywords, &obj, &number)) {
        return NULL;
    }

    /* Function implementation starts here */

    if (number < 0) {
        PyErr_SetObject(PyExc_ValueError, obj);
        return NULL;    /* return NULL indicates error */
    }

    Py_RETURN_NONE;
}

/*
 * List of functions to add to moduletest in exec_moduletest().
 */
static PyMethodDef moduletest_functions[] = {
    { "example", (PyCFunction)moduletest_example, METH_VARARGS | METH_KEYWORDS, moduletest_example_doc },
    { NULL, NULL, 0, NULL } /* marks end of array */
};

/*
 * Initialize moduletest. May be called multiple times, so avoid
 * using static state.
 */
int exec_moduletest(PyObject *module) {
    PyModule_AddFunctions(module, moduletest_functions);

    PyModule_AddStringConstant(module, "__author__", "ANIX");
    PyModule_AddStringConstant(module, "__version__", "1.0.0");
    PyModule_AddIntConstant(module, "year", 2018);

    return 0; /* success */
}

/*
 * Documentation for moduletest.
 */
PyDoc_STRVAR(moduletest_doc, "The moduletest module");


static PyModuleDef_Slot moduletest_slots[] = {
    { Py_mod_exec, exec_moduletest },
    { 0, NULL }
};

static PyModuleDef moduletest_def = {
    PyModuleDef_HEAD_INIT,
    "moduletest",
    moduletest_doc,
    0,              /* m_size */
    NULL,           /* m_methods */
    moduletest_slots,
    NULL,           /* m_traverse */
    NULL,           /* m_clear */
    NULL,           /* m_free */
};

PyMODINIT_FUNC PyInit_moduletest() {
    return PyModuleDef_Init(&moduletest_def);
}
