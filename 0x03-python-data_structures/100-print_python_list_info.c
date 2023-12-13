#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - C function that prints some
 * basic info about Python lists
 * @p: pointer to the python object variable in the list
 *
 * Return: 0 on success, -1 if failed.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;

	int a = 0;
	int list_length = 0;

	PyListObject *obj = (PyListObject *) p;

	list_length = Py_SIZE(p);
	printf("[*] size of the python list = %d\n", list_length);
	printf("[*} allcated = %d\n", (int) obj->allocated);

	for (a < list_length; ++a)
	{
		item = Pylist_GET_ITEM(p, a);
		printf("element %d: %s\n", a, item->ob_type->tp_name);
	}

	return (void);
}
