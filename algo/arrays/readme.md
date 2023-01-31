# Description

Some notes about arrays in python

## License

GPL

## Arrays and Lists - Advantages

- The best feature of arrays is **random access:** we can access arbitrary items extremely fast with indexes.
  - **Complexity:** O(1)
- Quite an **easy data structure:** easy to understand and easy to implement as well.
- Arrays are fast data structures in the main
- Arrays are recommended when you want to manipulate the **last item** of the data structure or you want to access items with **known indexes**.

## Arrays and Lists - Disadvantages

- We have to know the number of items we want to store at compile-time: so it is not a dynamic data structure
  - If we run in a condition where the array is full, we will have to allocate a larger chunk of memory in the **RAM** (usually **2x** the size of the actual array)
  - We have to copy the existing items one by one to the new array.
  - **Complexity:** O(N)
- Operations like inserting items (in any positions different from **last item + 1**)  or deleting arbitrary items in the middle of the array will require shifting existing items. If, arbitrary insert and delete operations are the majority, arrays should be avoided.
  - **Complexity:** O(N)