# C 語言的幾個重要特徵
(包含 C++, Rust, Ada，相較其他高階語言，例如 Python, PHP, JavaScript, Go)

## 1. 控制記憶體分配和釋放
### 1A. 動態記憶體
- **動態記憶體(dynamic memory)**：在程序運行時所申請分配或釋放的記憶體。
- **靜態記憶體(static memory)**：由程序運行前，編譯時系統分配的記憶體。
- 類 C 語言使用 `malloc()` 或相關函數來分配動態記憶體，須明確指定大小(size)。
- 動態記憶體是作業系統實現的，語言本身不具此特性。

### 1B. 靜態記憶體儲存在 Stack
- **Stack (棧)**：作業系統創造出的虛擬記憶體結構，符合 FILO 規則。
- Stack 不是 C 語言特有的，需理解作業系統的記憶體布局概念。

### 1C. 動態記憶體儲存在 Heap
- **Heap (堆)**：歷史原因命名，與資料結構 heap 不同。
- [Heap 的名稱由來](https://stackoverflow.com/questions/1699057/why-are-two-different-concepts-both-called-heap)

## 2. 變數大小規定
- 所有變數都需指定佔用大小。動態變數需指定使用動態記憶體。

## 3. 缺少顯含的物件導向特性
- 沒有顯含的繼承(Inheritance), 多型(Polymorphism), 封裝(Encapsulation)。
- [相關討論](https://stackoverflow.com/questions/7985169/why-is-c-not-oop-if-it-has-structs)
- C 語言有 `struct`，但沒有 class。

### 範例：
```c
// 基類結構體
struct Base {
    int base_data;
};

// 派生類結構體
struct Derived {
    struct Base base; // 嵌套基類結構體
    int derived_data;
};

