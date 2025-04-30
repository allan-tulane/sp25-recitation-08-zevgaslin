# CMPS 2200 Recitation 08

## Answers

**Name:**Zev Gaslin
**Name:**Joshua Haddad


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
heappush: log(V) work, for loop of edges: E work, W(ElogV)
heapop: logV work
(E+V) heap operations, with (logV) per heap:
W = O(ElogV + VlogV) = W(ElogV)

Span: Each heap takes (logV) time. Can't be paralellized becuase recursive, so can do V heaps at a time, so span is O(VlogV)

