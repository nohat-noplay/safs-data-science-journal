Private wrapper 
- Intended to only be used within the class/module in which it is defined. 
- Users will not directly call or interact with it as it’s internal.
- An underscore before the class name means “private”

`Def _binarySearchRec(sortedArr):`

Public wrapper
- Public interacts with and that method could call the private method.
- It isn’t any different to a normal function
`Def binarySearch(sortArr, target):
               `Return self._binarySearchRec(target)`