#include <stdio.h>
#include <Python.h>
/**
 *print_python_list_info - function that prints basic info about Python lists
 *@p: python list object
 *return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int index;
	PyListObject *pp;

	pp = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (index = 0; index < pp->ob_base.ob_size; index++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
	}
}
