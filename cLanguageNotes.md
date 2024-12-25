# Chapter_1. c語言(軟性包含c++, rust, ada)的幾個重要特徵(相較其他高階語言, 例如python , php , javascript, go)
  * ## 1. 記憶體管理, 分配和釋放
    * ### 1A. 動態記憶體(dynamic memory, 儲存在heap)
      * **動態記憶體(dynamic memory)**: 在程序運行時所申請分配或釋放的記憶體. 
      * **heap(堆)**: 它並不符合資料結構heap, 即優先佇列的規則, 只是因為歷史問題才以此命名, 是動態記憶體的實現區域.[Heap 的名稱由來](https://stackoverflow.com/questions/1699057/why-are-two-different-concepts-both-called-heap)
      * 在c語言中需要明確寫出申請及釋放. 任何語言都有動態記憶體, 不是只有c有, 只是其他高階語言通常自動化處理, 不須由程序員在代碼中寫出. 這有好有壞, 好處是方便, 較不會有遺漏, 壞處就是高階語言通常由c寫成, 由C實現動態記憶體管理, 類似於用原子拼成化合物, 會失去細緻度, 在處理底層細節優化時較沒有彈性.
      * 類C語言使用 `malloc()` 或相關函數來分配動態記憶體, 須明確指定大小(size). 這個size要由程序員本身自己記錄(透過程序的方式), 系統會分配一段動態記憶體給變數. 
      * 需要注意的是, 動態記憶體是作業系統實現的虛擬記憶體結構, 不是語言本身的特性, malloc使用作業系統提供的system call, 也就是說"c語言可以控制記憶體"這句話是有問題的, 原始沒有任何函數庫及作業系統支持的c語言只有靜態記憶體(任何程序語言其實都是), 他獲取的記憶體是由你設定的變數大小及多寡決定, 唯一讓c語言與其他高階語言不同的是, 他在語法上支持"指標\*", 和"取值\&", 這讓c語言在語法上可以直接指定某個記憶體地址的值是多少, 其他高階語言通常沒有關於記憶體地址的操作的直接語法. 其他的高階語言的編譯器將記憶體操作有關的動作全部"幫你寫完了", 讓程序在運行時自動檢查記憶體是否溢出. 但由於這個"記憶體是否溢出"的檢查機制是通用型的, 而不是針對所有程序邏輯中的個別情況, 這部分的操作就失去彈性了, 我們常說"c語言高效", 以為c語言本身特別厲害, 其實正好相反, c語言沒有提供任何自動化的記憶體操作, 你反而能自己針對各種適用的情況去設計關於記憶體的代碼, 理論上好的設計會更比高階語言的自動化記憶體管理機制更高效, 因為她是客製化的. 可以理解成c語言是直接去做一件事情, 其他高階語言則是去做一件事情及可能會衍生的麻煩問題連帶檢查和防止. 所以我們說c語言效率更好, 是不精確的, 應該說她的彈性更大. 由於"做一件事情"本身已經是最基本的單位了, 所以很多程序語言是c編寫並實現的. 

    * ### 1B. 靜態記憶體(static memory儲存在Stack) 
      * - **靜態記憶體(static memory)**: 由程序運行前, 編譯時系統分配的記憶體. 
      * - **Stack (棧)**: 作業系統創造出的虛擬記憶體結構, 符合 FILO 規則. 即靜態記憶體的實現區域. 
      * - Stack也不是 C 語言特有的, 是作業系統實現process記憶體的一部份, 需理解作業系統的記憶體布局概念. 

  * ## 2. 變數大小規定
    * ### 2A. 所有變數都需指定佔用大小, 動態變數需指定使用動態記憶體.

  * ## 3. 缺少顯含的物件導向特性
    * c語言沒有顯含的繼承(Inheritance), 多型(Polymorphism), 封裝(Encapsulation). 因此語言特性本身不具物件導向精神(雖然這些功能仍舊可以實現).[相關討論](https://stackoverflow.com/questions/7985169/why-is-c-not-oop-if-it-has-structs)
    * c語言沒有class, 但有`struct`, 這個東西可以建立"type", 所謂type就是int, char之類的變數類型, 且struct可以賦予內在元素, 例如struct dog{ int height, int weight}; 類似這樣, 已經有class的雛型, 只是struct沒有顯然的繼承功能必須要用嵌套的方式類似以下:
      * ```c
        // 基類結構體
        struct Base {
            int base_data;
        };

        // 派生類結構體
        struct Derived {
            struct Base base; // 嵌套基類結構體
            int derived_data;
        };
        ```
  * ## 4. c語言函數中的參數都是pass by value
  * ## 5. c語言函數中不是變數
    * 跟python不一樣, 在python中, 函數本身也是一個物件, 跟變數一樣, 你可以把它當成變數使用, 但是c語言中當你宣告或定義一個函數int testFunc();, 實際上int只是告訴編譯器testFunc()這個函數應該返回甚麼型態的變數. 
      * 函數在編譯後, 函數的機械碼會放在代碼段(Code Segment或Text Segment), 內存區域分成stack, heap, 數據段(data segement)以及代碼段(code segment, 只讀以防運行時被修改), 這是由於函數是程序邏輯, 他不像變數有固定大小, 這也意味在代碼中你不能任意將函數指定給某個變數或是讓變數指定給某給函數或函數指定給函數, 這是因為c語言編譯器在執行指定動作時, 需要確切的記憶體空間去紀錄和調派這些數據, 但是你不知道函數的大小(除非你特別去計算它的大小, 但這個應該挺麻煩), 所以這個功能c語言沒有做實現, 但實際上也不需要, 因為函數有指標, 你要傳遞或指派函數, 只需要用函數的指標即可(即函數的地址), 這實際上在效率層面更為快速, 而大家也都是這麼做的, 例如你在A函數, 想要使用一個函數作為其變數(這樣的目的是為了靈活性, 函數可以換成其他函數), 你只需要int funcA(int (*func)(int)){//do something}, 這樣你的func可以替換各種函數, 增加funcA靈活性(其實就是泛函數的概念), 這在c語言需要用指標, 在python中直接傳遞函數作為參數即可. 
      * 由於c語言中, 函數的以上特性, struct以及union結構中想要包含函數, 同樣要使用指針的形式宣告. 另外函數的名稱作為參數傳遞, 會自動退化成函數地址(聰明的設計, 與以上特性自洽)



# Chapter_2. C語言array的重要特性整理:
  * ## 1. array在創建的時候:
    * 編譯器似乎僅是記住了"首個元素的地址", 以及該array所對應的size, 還有類型.
  * ## 2. array在code中絕大部分的時候:
    * 編譯器都會自動把它當成第一個元素的地址
  * ## 3. 少部分時候: 
    * 在需要取得該array某些特性的時候, 例如取得size時候使用sizeof(), 或是取得地址使用&array的時候, 會將"首個元素地址"以外的size參數或者類型納入. 但需要注意的是, 在函數傳參的時候, 例如int testFunc(int *arr){}, array會退化為第一個元素的地址, 即便使用double pointer, int testFunc(int **arr){}也無法獲得size. 只有在struct中, array的從外獲取可以保留array特性, 例如typedef struct arr{int array[5];} arr, 在函數中int testFunc(arr *testArr){testArr->array};函數testFunc()可以獲得array的完整特性(包含size).
  * ## 4. 用來表示地址的變數
    * 也就是pointer, 有類型區別, int地址與char地址是不同類型, 而array地址同樣有自己的類型, 這個array類型包含了"首個元素地址", "大小", "元素類型", 而array的首個元素同樣有自己的類型, 包含了"自己的類型", "大小(例如整數佔據4byte), 我們會用首個byte的地址來表示該變數pointer地址, 所以你會發現array的第一個元素與array本身的地址"表示方式"一樣, 但你要清楚知道pointer有類型區別, array的地址數值上與array首個元素地址相同, 但所指的東西其實不是一樣的, array的第一個元素是屬於array的其中一員, 類似array是一個班級, 而首個元素是班級裡班長. 還需要再清楚說明一個概念, 例如整數占了4 bytes(也就是2^32次方bit), 現代計算機, 記憶體一般一個地址表示一個byte, 這是內存最小單位. 而一個整數的pointer, 有4 bytes, 卻是使用4個中的第一個來表示該整數pointer. 那如果有個變數類型占了6個bytes或是8個Bytes或是其他數量的bytes,你必須記錄"大小"來區分他是甚麼類型, 尤其array, array同樣用他的第一個byte來表示他的地址, 與array用他的第一個byte來表示他的地址
  * ## 5. 地址的取值方式(其實隱含array的本質)
    * 假設有個pointer指標, 宣告int *a, 則pointer指標變數a你有兩種取值方式, 
      * 第一種: 就是直接使用*a, "*"本身就是取值的意思, 你在宣告的時候int *a, 其實即是a取值後指向int, 所以a是一個存放int變數地址的指標. 
      * 第二種: 使用a[0], "[0]"本身的意思, 就是對指標a當下的指向進行取值, 而[1]就是對指標a的下一個元素進行取值, 以此類推.
      * 以下這段代碼充分展現了"地址取值", 以及下一個地址元素取值的精神:
        * ```c
		  #include <stdio.h>
		  #include <stdlib.h>

		  void main() {
			  int a = 1;
			  printf("a: %d\n", a);
			  printf("(&a)[0]: %d\n", (&a)[0]);
			  printf("(&a)[1]: %d\n", (&a)[1]);

			  printf("###########\n");

			  int b[3] = {1, 2, 3};
			  printf("b[2]: %d\n", b[2]);
			  printf("(&(b[1]))[1]: %d\n", (&(b[1]))[1]);
            }
          ```

# Chapter_3. c語言, 變數型別的修飾詞(need to keep in mind):
  * ## 3A.存儲類型說明符（Storage Class Specifiers）
    * **auto**：自動變數，默認局部變數類型。
    * **register**：寄存器變數，提高訪問速度，無法取地址。
    * **static**：
      * **靜態局部變數**：跨函數調用保留值。
      * **靜態全局變數/函數**：僅在本文件內可見。
    * **extern**：外部變數或函數，在其他文件中定義。

  * ## 3B. 型別修飾符（Type Qualifiers）
    * **const**：常量，不可修改。
    * **volatile**：告訴編譯器變數可能被外部修改，禁止優化。
    * **restrict(c99加入)**：唯一引用指針，允許編譯器優化。

  * ## 4B. 函數傳參時可否用修飾詞
    * 其實c語言的函數被調用時，函數的參數會在函數的內部創建一個"新的變數"，並將調用時傳入的值賦給這個變數。 也就是說架設int testFunc(int testVar) {}, 實際上int testVar就是等於在testFunc內宣告一個int testVar, 而他的值是所傳遞參數的值. "型別修飾符"可以直接在傳參時使用, 例如int testFunc(const int testVar) {}是合法的. 但是"儲存類型修飾符"則否, 我找不太到原理, 但是我推測是函數會在不同地方使用, 每次使用參數(是一變數)都會重新創建, 而static, extern, register等等是不能重新創建的, 他們是在函數第一次使用就必須"記住"的參數, 你每次使用都會記住上次的狀態.
    * A function parameter variable is a local variable (see Local Variables) used within the function to store the value passed as an argument in a call to the function. Usually we say “function parameter” or “parameter” for short, not mentioning the fact that it's a variable.
      * **static**：局部變數在函數多次調用中保持其值，並在程序生命周期內存在。這在函數參數中是無意義的，因為函數參數本身就是臨時變數。
      * **extern**：用於聲明一個全局變數或函數，表示它是來自其他文件的。這在函數參數中也無意義，因為參數本身就在函數內部。
      * **register**：建議編譯器將變數存儲在寄存器中，以提高訪問速度。但對於函數參數，編譯器會自行決定是否需要將其存儲在寄存器中，因此不需要顯式指定。

# Chapter_4. c語言如何import或include其他c文件的東西? 
  * c語言程序要執行一定要有main()作為程序入口, 沒有main()函數的c語言文件表示他是用來定義函數(或變數或結構)的文件, 大部分的專案此類型的c語言文件會佔到絕大多數(其實就和其他語言一樣, 只會有一個程序的main"入口"), 
  * 通常一個可執行專案都會有一個main.c(或是一個通用入口文件, 這點與其他語言也是一樣的, 從模組化角度來講main.c文件中越少定義函數而越多調用其他文件的模組自然越好, 但這類入口文件也有可能會定義學多函數, 通常是方便作初始畫或是起始畫功能, 例如redis裡面的server.c就定義了不少函數)
  * 如果一個專案沒有main.c(或入口文件)代表這個專案可能是"lib", 供給別人人使用的庫專案. 
  * c語言中通常使用頭文件(.h文件)進行函數或變數的宣告(只有宣告), 在.c文件中完成函數的邏輯定義. .c文件若要用到其他.c文件定義的模組功能, 只要引用.h中對該模組的宣告即可, 以下是一個極度簡化的範例:
    * ```c
      //file1.h
      #ifndef FILE1_H
      #define FILE1_H

      extern int sharedVar; // 聲明變數
      void printSharedVar(); // 聲明函數

      #endif // FILE1_H
      ```
    * ```c
      //file2.c
      #include "file1.h"
      #include <stdio.h>

      int sharedVar = 10; // 定義變數

      void printSharedVar() { // 定義函數
          printf("sharedVar: %d\n", sharedVar);
      }
      ```
    * ```c
      //main.c
      #include "file1.h"
      #include <stdio.h>

      int main() {
          sharedVar = 20;
          printSharedVar(); // 調用函數
          return 0;
      }
      ```
  * 以上範例, 你會發現.c文件並沒有被main.c引入, 只有頭文件.h被引入. .c 的內容並不會因為引入 .h 自動讀取. 當你包含頭文件（例如 file.h）時. 實際上只是告訴編譯器該文件中聲明了某些函數和變數, 但並沒有包含它們的定義. 這些定義仍然必須在編譯過程中被明確引用. 對程序開發者來說, 你只要引入.h文件(並且你有把對應的模組寫好), 基本就等於引入模組了.(詳細解釋請見Chapter_8的筆記)
  * 另外一點需要注意的是, c語言include頭文件是有傳遞效果的, 例如test.c include A.h, 而A.h又include了 B.h, 則對test.c而言, 他相當於include了B.h
  * 有些專案中會對某些頭文件進行條件編譯, 以免被重複引用, 這招有時稱作"頭文件保護", 例如一下範例:
    * ```c
	  #ifndef B_H
  	  #define B_H

	  #define B_DEFINITION 1

	  void functionB();

	  #endif // B_H
      ```

# Chapter_5. c語言編譯過程(可一步步自行實驗, c\++和c在編譯上幾乎一樣, 只是gcc變成g\++), 
  * ## 5X. c語言最常用的編譯器
    * (正式專案中也是最常用的)是GNU Compiler Collection, 即是gcc, 所以以下都用gcc為範例:
  * ## 5A. 預處理(preprocessing)：
    * 功能和目的: 處理頭文件包含（#include）、宏定義（#define）、條件編譯（#ifdef）等指令, 其實就是把代碼微調成真正要編譯的代碼。
      * 命令示例:
        * ```bash 
          gcc -E main.c -o main.i
          ```
      * 結果: 生成預處理後的文件 main.i, .i文件實際上.c文件的預處理後擴展形式, 同樣是純文字檔案, 在語法上, 他比c語言多了"行號指令", 告訴編譯器接下來從甚麼文件的甚麼行號開始編譯, 可以說.c文件是.i文件的子集合.
  * ## 5B. 編譯(compiling): 
    * 功能和目的: 將預處理後的源文件轉換為匯編代碼。
      * 命令示例: 
        * ```bash 
          gcc -S main.i -o main.s
          ```
      * 結果: 生成匯編代碼文件 main.s, 這個main.s就是匯編語言的純文字檔案, 他的匯編語言是根據你使用的cpu架構指令集. 最常見的應該是x86 和 x86_64 架構, 也就是intel的指令集語法. 理論上編譯器會自動監測你的CPU使用甚麼架構(通常桌機用x86/x86-64, 手機用ARM), 但是你也可以也應該要可以自己指定匯出的匯編文件使用甚麼指令及架構:例如: gcc -march=x86-64 -o myprogram myprogram.c   需要注意的是, 許多語言沒有生成匯編語言的步驟, 這並不奇怪, 因為會編語言實際就是"指令集"的組合操作, 他把bin機械碼的指令與人類可讀的英文去做對應, 讓人們可以直接用英文去撰寫對CPU所要執行的一系列指令操作. 所以生成匯編語言完全可以不必, 只要編譯器知道bin機械碼的指令集即可(反正人類不需要讀), 而c語言保留生成匯編語言的步驟, 除了兼容性, 一方面也是因為可以更加靈活, 想像你在匯編的階段還能再對最終結果做出一些調整, 這對編程的彈性可以說相當大了. 順帶一提彙編語言是要成為頂級電腦高手必學的項目之一, 用來進行"極限優化"的情況, 例如嵌入式系統或是一些3A遊戲. 
  * ## 5C. 匯編(assembling): 
    * 功能和目的: 將匯編代碼轉換為機器代碼，生成目標文件（.o 文件）。
      * 命令示例: 
        * ```bash
          gcc -c main.s -o main.o
          ```
      * 結果: 生成目標文件 main.o, 這一步驟將匯編語言文件轉成bin文件.
  * ## 5D. 鏈接(linking): 

# Chapter_6. 進階編譯
  * Chapter_5中提到的是一個過度簡化的範例, 方便理解基礎概念, 實際上所需編譯的文件可能十分多, 並且文件之間關係複雜, 單純只用gcc十分難以處裡, 你需要一個script來有效率的執行gcc, 這個其實就是Makefile以及make了(事實上絕大多數稍有規模的專案都會使用make及Makefile). Makefile實際上就是指揮編譯器如何編譯的script(txt文件), 而make則是執行Makefile的指令(與gcc相互獨立不隸屬), Makefile中可以指定所需使用的編譯器(最常使用的就是gcc). 以下是一個Makefile的簡單範例[討論參考](https://stackoverflow.com/questions/768373/what-is-the-difference-between-make-and-gcc):
    * ```makefile
	  # 定義編譯器和編譯選項
	  CC = gcc
	  CFLAGS = -Wall -g

	  # 定義目標文件和源文件
	  OBJS = main.o example.o
	  TARGET = myprogram

	  # 默認目標
	  all: $(TARGET)

	  # 生成可執行文件
	  $(TARGET): $(OBJS)
	      $(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

	  # 編譯主程序
	  main.o: main.c example.h
	      $(CC) $(CFLAGS) -c main.c

	  # 編譯例子模組
	  example.o: example.c example.h
	      $(CC) $(CFLAGS) -c example.c

	  # 清理生成的文件
	  clean:
	      rm -f $(OBJS) $(TARGET)
      ```
    * Makefile在較大型的專案中可能會變得很複雜, 這個時候有些自動撰寫Makefile的工具, 例如cmake或是automake

# Chapter_7. 預處理
  * 由於預處理是常用的功能, 我們單獨拿出討論, 只要看到"#"即表示預處理的意思, 在文件未正式進入編譯狀態時, 所要處理的事情, 包括#include, #define(即宏, 其實就是文本替換, 沒什麼複雜的), #if(條件編譯, conditional compiling), 等於你可以指定文件中特定的部分如何編譯. 
  * **宏(即macro, 又稱巨集)**: 是編譯過程中非常常用到的東西, 本質就是文本替換, 有分"有值宏"和"無值宏": 
    * 有值宏如下:
      * ```c
	    // 主要功能是替換文本
		#define pi 3.14
        ```
    * 無值宏如下:
      * ```c
	    // 主要功能是作為"開關", 
		#define feature_enable
        ```
      * 無值宏通常會搭配#if defined()使用, 判斷該宏是否存在, #if defined(macro_name)等價於#ifdef macro_name. 在許多情況下, 有些宏(macro_name)是由系統自動產生, 無須programmer建立, 離如作業系統名稱WIN32. 由於很多專案會使用條件編譯, 所以無值宏看似無用, 其實很常使用, 在很多開源的專案都可以看到.
	
# Chapter_8. c語言為何需要.h(header)文件?
  * 如果.h文件只是宣告函數和變數, .c文件中其實定義函數的時候不就已經順便宣告? 如此一來為何還需要.h??[reference](https://stackoverflow.com/questions/2184646/what-is-the-point-of-header-files-in-c), [reference2](https://www.reddit.com/r/C_Programming/comments/cc1gn9/why_do_header_files_exist/)
    * 最終理解: 在最早的時候, 記憶體匱乏, 如果採用現代語言編譯器的方式, 直接用函數定義文件中的函數宣告來做為引入執行文件的方式, 會導致編譯器需要把整個定義文件丟入記憶體中, 但實際上你只需要"函數的宣告(函數名稱, 輸入以及輸出所需的變數及變數大小)"就可以生成可用的執行文件. 例如一個宣告一個函數int func(int var); 不管此函數的定義(implement)是如何, 可是簡單的平方或乘上某數, 不管計算內容為何, 你編譯後的文件, 例如func.o, 實際上是"可用"的, 只要最後把函數定義的編譯結果, 在要使用的時候, 去尋找來用即可, 所以實際上你只需要函數的宣告文件來編譯可執行文件. 如果採用現代編譯器的方式, 直接函數定義文件(本身其實就包含宣告)中尋找函數的宣告來編譯執行文件, 對開發者而言是較為省力, 因為你不用再去維護header檔案, 但是函數定義文件通常較大, 這意味著編譯器對每一個執行文件編譯時, 都需要把函數定義文件載入記憶體去進行尋找宣告的動作, 這在早期記憶體昂貴的情況下, 是不現實的(且也會耗費一定的算力). c語言之所以仍舊保留使用header文件, 一方面是因為兼容性問題, 一方面也是因為速度較快(雖然我認為這個速度差別可能微乎其微).

# Chapter_9. typedef, struct
  * typedef最直接的用法如下:
    * ```c
	  typedef type new_type;
      ```
    * 這是最簡單的用法, 雖然是最簡單的, 但實際上仍舊會在實際情況看到, 這種用法看似沒有意義, 如果定義了一個新變數類型new_type, 但是這個new_type完全就是type, 那何不用type? 這是因為如果當我們在其他地方使用這個new_type, 而如果哪一天需要修改成typedef type2 new_type; 我們就不需要把有new_type的地方全部改掉, 並且new_type的變數命名可以針對我們想要的情況, 已讓代碼可讀性提高.

  * struct new_struct宣告後, 如果要取得結構內的元素, 可直接使用new_struct.attr1, 如果是struct的地址, 則可以使用(&newstruct)->attr1
    * ```c
      #include <stdio.h>
      #include <stdlib.h>

      struct teacher {
          int age;
          int gender; // 1 for male, 0 for female
      };


      int main() {
          struct teacher peter;
          peter.age = 1;
          printf("show teacher peter's age: %d\n", peter.age);
          printf("------------------------\n");
          struct teacher *alice_p;
          alice_p->age = 2;
          printf("show teacher alice's age: %d\n", alice_p->age);
      }
      ````
    * 需要注意的是struct內定義元素, 是無法進行初始化的, 也就是說struct {int testValue = 1;} 這樣做是違法的, 只能struct {int testValue;} 然後事後再進行元素賦值

# Chapter_10. enum關鍵字
  * **enum**, 即是"enumeration(枚舉)", 這關鍵字是一個"類型"宣告, 與int, char是一夥的, 他的定義語法比較特別, 其他語言似乎沒有這類的東西, 且聽我慢慢解釋, 理論上他是有用且有意義的, 簡單舉例來說enum day {sunday, monday.....};你宣告了day這個enum變數, 則day的數值只能能是sunday, monday.....它裡面所類舉的"枚舉常數", sunday, monday...他們的作用與宏(macro, #define)是一樣的, 不指定數值的話, 默認是從0, 1, 2, 3的值開始賦予(也就是sunday=0, monday=1....). 與宏不同的是, "枚舉常量"會受作用域(scope)的限制, 這增加了靈活度. 而由於day受到"枚舉常量"限制(只能是枚舉常量中的其中一個值), day避免了被賦予超過範圍值的可能性, 這是一種安全上的優勢. 需要注意的是day被"枚舉常量"限制, 但是"枚舉常量"本身沒有被其他變數使用限制, 也就是你完全可以新增一個變數int testVar=Sunday; 只要scope允許就好. 以上我提到的枚舉常量限制只是c語言理論上如此, 實際上我使用編譯去測試, 發現編譯器對garbage value沒有限制, 只對使用其他enum變數的常量做出限制, 例如
    * ```c
      enum day {sun, mon, tue, wed, thu, fri, sat};
      enum month {jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec};
      enum day d = jan;   // error
      enum month m = tue; // error
      d = 1234;
      m = -5;	
      ```
  * 在實際測試了之後, 發現gcc連以上的範例都沒有任何限制, enum變數的值可以隨意指定, 也就是說enum只是讓代碼的可讀性增加了, 並沒有真的達到安全的效果(有點雞肋的功能, 或者c語言本來就不關心安全問題), 感覺它更像是macro的升級版, 以下參考和討論:
    * [referenec_1](https://www.reddit.com/r/C_Programming/comments/1efydnn/do_i_understand_enums_right/)
    * [reference_2](https://stackoverflow.com/questions/21683289/enum-in-c-is-not-throwing-an-error-on-invalid-input)
    * [reference_3](https://stackoverflow.com/questions/22646165/what-is-the-use-of-enums-in-c-and-c)

# Chapter_11. goto關鍵字, 
  * 純屬無用的雞肋功能, 用於跳過某些代碼到某些段落, 但通常建議使用if, for, while, loop等方式代替實現, 避免代碼產生混亂, 它存在意義就是讓人知道, 再優秀的語言都有缺點, 以下是範例:
    * ```c
	  #include <stdio.h>

	  int main() {
	      int value = 5;

	      if (value == 5) {
	  	goto skip;  // 跳轉到標籤 skip
	      }

	      printf("This line will be skipped.\n");

	  skip:
	      printf("This line will be printed.\n");

	      return 0;
	  }
      ```

# Chapter_12. volatile"型別修飾符" 
  * 修飾變數用的, 與c語言的編譯器的"優化"功能有關, 所謂"優化"指的是, 編譯器在編譯過程, 會盡量節省不需要的計算和指令, 以耗費最少的資源達到程序代碼所能達到的目的和效果. 例如某段代碼int flag = 0; while (flag == 0) { // 某些操作 }, 如果編譯器假設 flag 在這個 while 循環內部不會被改變，那麼它可能會優化這段代碼，使得 flag 僅在循環開始時檢查一次，而不是每次迭代都重新讀取 flag 的值。這樣的假設在普通情況下是安全的，但是如果 flag 被標記為 volatile，這意味著它可能會被程序的其他部分或外部事件（如硬件中斷）改變，編譯器就不能做這樣的假設。這裡是一個較為詳細且有深度的[說明](https://blog.csdn.net/LoseInVain/article/details/103356324)
  * 要徹底理解volatile的作用, 必須要把寄存器(register)和內存的關係理解清楚. 首先register和ram都是記憶體(memory), 記憶體分層叫做memory hierarchy, register是最快的記憶體, 是CPU中的一個重要部件, 用來與CPU中ALU和CU組隊處理計算的一員, 他的主要工作是用來暫存"ALU"所要處理的數據, ram則是在CPU之外的記憶體, 他是用來臨時存放"CPU"所要處理的數據. 如果你直接寫匯編語言, 你就會發現, 其實匯編語言主要在做的事就是把RAM的數據放到register, 經過計算後再把register的數據放回ram. 而c語言compiling的過程會生成匯編, 你可以清楚發現編譯器有時候會做些優化, 在明知變數不會改變的情況下, 省去一些把重複讀取ram或是放數據進ram的指令動作, 用以提升效能(因為ram慢), volatile就是告訴compiler不要做這些動作, 因為變數可能在讀取ram後或放入ram前改變.

# Chapter_13. const"型別修飾符" 
  * 建立並使變數變成唯讀, 一方面保護數據被修改, 一方面增加代碼可讀性

# Chapter 14. restrict"型別修飾符" 
  * 專門用在pointer的, 他與volatile都與編譯器的"優化"有關. 簡單來說假設宣告變數restrict int *a; 則a所指向的地址只能由a記錄, 意思是假設a = 0x1234, 則int *b不能等於0x1234, 除了a以外, 其他pointer變數不能指向與a相同的地址. 假設不使用restrict, 編譯器會默認, 指針a和指針b可能指向同一個地址, 這樣操作a, b的讀寫時, 指令的順序變得很重要, 因為如果一個指針寫入數據，另一個指針讀取數據，編譯器必須保證讀取操作發生在寫入操作之後，否則會導致數據不一致. 如果編譯器不知道指針是否指向同一個位置，它可能需要在每次使用指針時都進行內存訪問，以確保最新的數據被讀取。這樣就無法將數據保存在寄存器中，從而影響性能. 舉例來說, 循環優化(就是迴圈優化, 讓重複性高的動作能減少一些計算資源)可以透過迴圈代碼的修改(優化效果有限), 也可以在編譯的步驟進行優化, 例如範例: 
    * ```c
      void add_arrays(
          int *a, 
          int *b, 
          int *c, 
          int n) {
          for (int i=0; i<n; i++) {
              c[i] = a[i] + b[i];
          }	
      }
      ```
    * 此範例, 每一次的loop都要從ram讀取a, b, c, 如果編譯器知道a, b, c都是唯一指針, 則可以將數據放在register讀取或寫入, register比ram快得多, 這樣速度就上來了.

# Chapter_15. auto"存儲類型說明符"
  * 用於聲明自動變量，這些變量的作用域僅限於其所在的代碼塊（例如函數或語句塊），並且在代碼塊結束時自動銷毀。auto 是C語言的默認存儲類型，因此大多數情況下即使不顯式使用 auto 關鍵字，編譯器也會默認將變量視為自動變量. 也就是說你幾乎用不到auto

# Chapter_16. static"存儲類型說明符" 
  * static修飾的變量的存儲空間在程序運行期間始終存在，即使函數結束也不會被釋放。也就是說一般變數的生命週期是依賴於其scope(如果被定義在函數中則依賴函數生命週期), 而使用static則生命依賴於整個程序, 程序終止才消逝. 這使得函數內的static變數在函數被不同時機調用時, 可以保持之前的"記憶", 直到程序終止. static還有個特徵, 就是他強制限制scope, 無論是變數還是函數, 只要加上static, 就只能在該scope可見, 例如int testFunct(){static int testVar;}, 則testVar只在testFunct()內可見, 如果是全局, 則在該文件中可見, 函數也是如此, static int testFunct();只在該文件可見. 簡單來說static除了讓變數及函數的生命週期依賴全域(整個程序), 且可見性強制遵守scope(不過變數本身其實已經幾乎都遵守scope了)

# Chater_17. extern"存儲類型說明符"
  * external之意, extern主要在.h文件中使用, 它的目的是解決變數宣告只限於局部的問題. 簡單來說, 函數的宣告本身就是全局宣告了, 他可以在任何文件中被認出, 而一般的變數宣告只是局部宣告(只能在本文件被認出). 假設我們在module.h頭文件宣告函數及變數void testFunc(){// do something;} int testVar; 然後在module.c中定義testFunct及testVar, 例如void testFunc(){printf("test");} int testVar = 1; 函數testFunct本身沒有問題, 可以使用, 但是testVar就有問題了, 因為編譯器會把module.h的testVar以及module.c的testVar當成不同東西, 而main.c引入module.h只會引入module.h的testVar. 要讓testVar能夠像testFunc被全局看見, 則module.h需要變成void testFunc(){//do something;} extern int testVar;這樣編譯器才知道module.h的testVar宣告由其他文件中完成定義. 也可以理解成函數本身就默認是extern(所以函數不須加extern), 而變數則否. 基本上你看到的任何在.h文件中宣告的變數, 都會加上extern(你可以去看一些開源專案). 表示此變數的定義會在其他文件中完成.

# Chapter_18. register"存儲類型說明符" 
  * 用於提示編譯器將變量儲存在CPU的寄存器（register）中，而不是在內存中。這樣做可以提高變量的訪問速度，因為寄存器比內存訪問更快。不過，這僅僅是一個提示，編譯器並不一定會遵循這個建議，特別是在寄存器資源有限的情況下。簡單講register變數就是當寄存器有空閒則優先讓其存入. 由於寄存器不像內存有"地址", 所以compiler不允許取址動作(就算該變數暫時不在register內也無效)

# Chapter_19. 作用域(scope) 
  * c語言的作用域scope以**{**及**}**為界定, 這適用於多種情況，包括函數、條件語句、循環等, 例如以下代碼會出錯
    * ```c
	  int testFunc() {
	  	for(int i=0; i<10; i++){
	  		if(i<5){
	  			int result = 1;
	  		} else{
	  			int result = 2;
	  		}
	  		printf("Show the result: %d\n", result);
	  	}
	  }
      ```
    * 因為result只在if的"{}"可見, 在for以及testFunct()的"{}"都不可見.

# Chapter_20. break關鍵字
  * 此關鍵字會終止其所在的loop(包含for, while)或switch(只有最近的, loop之外的loop不會終止).

# Chapter21. continue關鍵字 
  * 此關鍵字用於跳過loop(包含for, while)內的"本次迭代", 進入下一個迭代.

# Chapter22. switch, case, default
  * case, default這兩個關鍵字與switch綁再一起, 不能獨立使用 
  * **switch**語句: 根據表達式的值, 選擇執行多個分支中的一個. 

  * **case**標籤: 指定當switch表達式的值匹配某個常量時, 應該執行的代碼. 

  * **default**標籤: 指定當所有case標籤都不匹配時, 應該執行的代碼. 

  * switch通常需要搭配break使用, 這是因為當一個 case 匹配後，如果沒有 break，程序將繼續執行後續的 case 標籤和其對應的代碼，這稱為“fall-through”行為. 例如你case1符合, 你沒有break, switch會把接下來的case2, case3...所有的case都執行一次. fall-through 行為在C語言中的設計主要是減少case中重複代碼的問題, 讓代碼簡潔一些, 這是因為不同的case很可能需要執行相同的事情, 例如以下(周一到周五上班, 周六周日放假)
    * ```c
	  #include <stdio.h>

	  void example(int day) {
	      switch (day) {
	  	case 1:
	  	case 2:
	  	case 3:
	  	case 4:
	  	case 5:
	  	    printf("Weekday\n");
	  	    break;
	  	case 6:
	  	case 7:
	  	    printf("Weekend\n");
	  	    break;
	  	default:
	  	    printf("Invalid day\n");
	  	    break;
	      }
	  }

	  int main() {
	      example(3);  // 輸出：Weekday
	      example(7);  // 輸出：Weekend
	      return 0;
	  }
      ```

# Chapter_23. union關鍵字 
  * 一種數據結構，允許在同一內存位置存儲不同類型的數據。這意味着，儘管 union 可以包含多個成員，但在任意時刻，只能有一個成員有效。union 的主要用途在於節省內存，尤其是在需要變量可以存儲不同類型的數據但同一時間僅使用其中之一的情況下
    * ```c
	  #include <stdio.h>

	  union Data {
	      int i;
	      float f;
	      char str[20];
	  };

	  int main() {
	      union Data data;
	      
	      data.i = 10;
	      printf("data.i : %d\n", data.i);
	      
	      data.f = 220.5;
	      printf("data.f : %f\n", data.f);
	      
	      snprintf(data.str, sizeof(data.str), "C Programming");
	      printf("data.str : %s\n", data.str);
	      
	      return 0;
	  }
  * union某種程度上是為了實現一個記憶空間可以使用不同型態的變數(c語言本來不行, 即使兩種不同變數型態占用相同大小, 仍舊不行, 因為c語言遵守嚴格類型檢查). 在上面範例中當data.str被指定後, data.i與data.f就失效了. 而union 的大小是它的所有成員中最大的那一個。這樣可以確保無論你訪問哪個成員，都有足夠的內存空間

# Chapter_24. for, while, do...while, 三種迴圈用法
  * for 循環通常用於需要明確初始化、條件檢查和更新語句的情況。它的結構清晰，適合有固定次數的循環。
  * while 循環適用於在進入循環之前不知道確切的循環次數，但需要在每次迭代之前檢查條件的情況。它更加靈活，可以處理基於動態條件的循環。
  * do while循環與 while 循環類似，但它會至少執行一次循環體，然後再檢查條件，這在需要先執行後檢查的情況下特別有用.  
  * 理論上這三種迴圈方式可以互相實現, 同時存在只是為了提高代碼的可讀性, 由於loop是時常使用到的程序技巧, 這是方便programmer. 需要注意的是c語言中do是搭配while一起使用的, 不能獨立運作, 因為do 語句是用來表示循環體應該至少執行一次，而 while 語句則提供了繼續執行循環的條件.


# Chapter_25. malloc()
  * 動態記憶體分配函數, 需要注意的是, malloc不是c語言的關鍵字, 以上提到的所有c語言用法都是c語言關鍵字, 但malloc()是來自#include <stdlib.h>, 你不引用stdlib是用不了malloc的. 但有個問題是, stdlib本身也是c語言寫成, 而純c語言沒有可以控制動態記憶體的語句, 那malloc是如何實現的?? 其實是這樣的malloc來自stdlib, 而stdlib則是調用"操作系統"提供的頭文件(linux提供unistd.h中的brk和sbrk和mmap函數, windows提供windows.h中VirtualAlloc和HeapAlloc等函數)所提供的動態記憶體分配功能. 但是!! linux操作系統本身也是c語言寫的, 那brk等等動態記憶體調用功能又是如何實現的? 因為c語言本身沒有支援動態記憶體分配, 那brk等等功能是如何實現的? 下一個筆記free standing中會有關鍵說明. 先明白一件重要的事實, 所謂動態記憶體和靜態記憶體, 並不是ram原有的性質, ram就是物理記憶體, 他沒有動態靜態之分, 是作業系統"實現"的, 事實上"virtual memory(虛擬記憶體)", "頁表(page)", "區(zone)", "heap", "stack", 這些東西都是由linux kernel利用程序邏輯實做出來的(c語言), 他們都是虛擬的, 是邏輯結構, 而非實體結構(可以查看linux關於記憶體管理的筆記). 
  * 補充注意: 的是heap內部對變數的記憶體分配不一定是連續的, 意味著假設宣告兩個動態陣列heap_array1, heap_array2, 他們可能分別在heap中的不同段, 不是連續在一起的, 這是作業系統設計用來方便調整大小, 而又由於為了避免兩個array增長後出現碰撞的情形, 作業系統會動態調整heap_array的起始地址, 你只要使用realloc()就會發現起始地址有可能會改變. 而array中所有的數據都要跟著移動, 這也是heap比較慢的原因之一, 因為有額外計算.
  * reference: 
    * [reference_1](https://www.cnblogs.com/lyxtech/articles/15187081.html)
    * [關於c語言需要調用sys_call, 則sys_call是如何被c語言寫出來的?](https://www.reddit.com/r/AskProgramming/comments/1bb6cfb/how_can_operating_systems_be_written_in_c/)
    * [下面有個回答提到了freestanding c environment(沒有任何Lib的c, 通常用在沒有作業系統的embedded system), 表示c在沒有任何lib的情況下依舊能夠寫出作業系統](https://www.reddit.com/r/learnprogramming/comments/1g8wnr8/how_can_operating_systems_be_written_in_cc_and/)
    * [關於freestanding c env的解釋](https://www.reddit.com/r/learnprogramming/comments/780vwv/c_what_is_the_difference_between_a_hosted_and_a/)

# Chapter_26. freestanding c environment(沒有任何lib及作業系統system call可用的環境, 部分純embedded system即是如此)
  * 一般在作業系統環境中使用的c語言叫做hosted enviornment
  * 一般的作業系統本身就是在freestanding c environment開發並運作的, 作業系統沒有也沒辦法使用標準庫, 因為標準庫本來就是作業系統需要實現的
  * 在freestanding中所有記憶體都是靜態記憶體(編譯時就已經分配好的記憶體空間), 由於沒有虛擬記憶體(因為沒有作業系統)，動態記憶體（Dynamic Memory）也不存在。動態記憶體是指在程式執行時動態分配和釋放的記憶體空間, 在沒有虛擬記憶體的環境下，程式的記憶體空間直接映射到實體記憶體上，沒有任何層級的間接映射。這意味著靜態記憶體、程式碼和資料都存放在實體記憶體中。在這種情況下，靜態記憶體、實體記憶體和硬體記憶體基本上是同義的，都是指實際的物理記憶體。也就是說你在freestanding 環境下(或是沒有作業系統的embedded system), 你宣告一個變數int var; 然後&var取址, 這個地址是物理記憶體地址! 而不是虛擬地址, c語言不管這個地址到底是不是虛擬的, 址管使用, 虛擬地址是作業系統控制的, 讓應用程序能在邏輯上使用連續記憶體, [這裡有個參考討論, 注意"Joe Zbiciak"的回答](https://www.quora.com/Why-do-C-pointers-use-virtual-memory-instead-of-physical-memory)
  * 在freestanding(或embedded system)中也不會有process進程的概念(這是作業系統創造的虛擬管理單元), 程序就是直接在記憶體中運作, 且通常embedded system只會反覆運行一隻程式, 這支程序會占用所有的資源, 是不是有點眼熟, 因為其實作業系統本身就是一種這樣的程序, 他本身就是一個超級複雜的"嵌入式系統程序", 獨佔了所有記憶體和硬體資源, 你在啟動及使用PC的時候其實就是在運行"作業系統"這隻程序. linux內核在用c寫成之時, 一開始肯定有宣告所有記憶體都是它的, linux運作中有其他任何使用者自己建立的程序(包含安裝或開發的), 都是運行在linux內核所建立的"虛擬環境(也就是虛擬記憶體)"上, 此時假設A應用程序需要記憶體的時候, 就跟linux內核要求, linux內核實際上是把自己占用的某段記憶體標記為"A應用程序占用"(實際上還是linux內核自己占用), 然後讓A使用該段記憶體. 等到A程序終止, 再將該段記憶體標記為"未使用"(實際上還是linux內核自己占用). 有了這個概念你瞬間就明白之前的malloc()函數的根本原理是甚麼了, c語言明明只有靜態記憶體, 為何還能創造出malloc, brk, mmap之類的動態記憶體分配函數? 理由其實是作業系統把自己占用的靜態記憶體借給應用程序使用, 假設A應用程序在運作時想要獲得額外的記憶體使用時, 便向kernel申請(也就是system call), kernel將自己正在占用的某段靜態記憶體標示為"A所申請的動態記憶體", 接著管理和分配. 這便是malloc的真相. 追根究柢, 根本沒有真正的"動態記憶體", 也可以說動態記憶體真的就只是"虛擬"的. 在freestanding c中, 記憶體宣告後, 是不能改變大小的, 也就是說linux kernel(freestanding c寫成)本身獲得記憶體後, 不能獲得額外的記憶體了, 但是他又負責指派記憶體給應用程序, 那唯一的可能就是, linux kernel宣告了所有記憶體, 所以她才能指派及分配記憶體. 換句話說, 若一台機器安裝了作業系統程序, 實際上這台機器在使用時只有在運作這個作業系統程序而已, 任何其他使用者自行安裝的應用程序, 其實都是在作業系統程序所建立的"虛擬邏輯狀態"之下運行的, 機器從頭到尾根本上只有運作作業系統這一個程序.

# Chapter_27. 最初的c語言編譯器是由B語言寫的, 而B語言由assembly寫的, 
  * [這是一個討論](https://www.reddit.com/r/cprogramming/comments/15jqywk/were_the_first_c_compilers_written_in_assembly/)

# Chapter_28. c語言的關鍵字(keyword)和識別字(identifier) 
  * 所謂**識別字(identifier)**就是變數名稱或函數名稱等等編譯器需要當作"名稱"的東西, 
  * **關鍵字(keyword)**實際上就是語言的保留字, 你會看到有些關鍵字是底線(underscore)開頭, 這些關鍵字都是在較為近代才加入的關鍵字, 因為比較少人會用底線開頭作為變數名稱, 為了不讓舊的代碼出現變數名稱與新關鍵字衝突, c語言就新增了一個規則, 就是以後所有新的關鍵字, 全部用底線開頭, 例如_Bool, _Alignas, _Atomic全部都是. [這裡有一些討論](https://stackoverflow.com/questions/56211904/why-does-c-have-keywords-starting-with-underscore)

# Chapter_29. buffer overflow, memory leak, stack overflow
  * c語言中管理記憶體時需要注意的問題. 這三種情況都只會發生在該程序的"進程記憶體空間", 通常不會影響其他程序或系統的記憶體空間。作業系統會為每個程序分配獨立的記憶體空間，程序只能訪問自己的記憶體空間，不能訪問其他程序的記憶體空間. 

  * ## 29A. buffer overflow, 
    * 其實就是程序操作了超過你宣告變數的記憶體範圍的記憶體, 可以簡單理解成buffer就是陣列, 所以buffer overflow其實就是array overflow, 例如你宣告一個int array[10]; 但程序在執行中的時候, 指派了array[11]的值, 這在程序中是可以辦到的, 你的代碼如果沒有實現檢查或防護機器, 又或者編譯器沒有編譯時加入這樣的機制的機械碼, 則會發生. 
    * 現代的編譯器(例如gcc)都有保護機制, 預設都會再編譯成機器碼的時候, 插入Stack Protector(堆疊保護)或Stack Canaries(堆疊金絲雀)機械碼, 若想要重現buffer overflow, 在編譯的時候(gcc), 你可以加入參數-fno-stack-protector, 取消保護機制, 也就是預設是保護, 但你完全可以取消. 
    * buffer overflow攻擊來自於對記憶體布局的"漏洞", 一般一個程序運行在一個process, 他的記憶體布局(在linux作業系統關於記憶體管理的重要筆記提到過), *高位地址*|stack||->...<-||heap||data||text|*低位地址, 假設我們的函數及變數都使用stack(heap也會有buffer overflow, 但原理類似, 故不多做贅述), 由於stack是有高位地址向下增長, 我們可以舉個例子如下:
      * ```c
		#include <stdio.h>

		void functionB(int a, int b) {
		    int result = a + b;
		    printf("Result: %d\n", result);
		}

		void functionA() {
		    int x = 10;
		    int y = 20;
		    functionB(x, y);
		}

		int main() {
		    functionA();
		    return 0;
		}
        ```
      * 則其stack內布局如下(符合先進後出):
        * ```txt
		  高位地址
		  ------------
		  | main的堆疊幀  | <- 包含main函數的局部變數等
		  | 返回地址: main | <- 指向main函數中調用functionA的位置
		  | 幀指標        | 即stack frame pointer, 即是該frame的位址(該frame最高位地址)
		  | 局部變數      |
		  ------------
		  | functionA的堆疊幀 |
		  | 返回地址: funA  | <- 指向functionA中調用functionB的位置
		  | 幀指標        |
		  | x = 10        | <- 局部變數 x
		  | y = 20        | <- 局部變數 y
		  ------------
		  | functionB的堆疊幀 |
		  | 返回地址: funB  | <- 指向functionB結束後返回到functionA的位置
		  | 幀指標        |
		  | a = 10        | <- 參數 a
		  | b = 20        | <- 參數 b
		  | result       | <- 局部變數 result
		  ------------
		  低位地址
          ```
        * 上面的佈局中有個東西叫做"stack frame", 先簡單說明一下其用處. 假設我們考虑进程执行时发生函数调用的场景，由於母函数和子函数會使用的是同一个stack，在通常的情况下，我们并不需要区分母函数和子函数分别使用了stack的哪个部分。但是，当我们需要在执行过程中对函数调用进行backtrace的时候，这一信息就很重要了。 简单的说就是一个函数所使用的stack的一部分，所有函数的stack frame串起来就组成了一个完整的栈。stack frame的两个边界分别由FP和SP来限定。
      * 剛才的布局範例沒有array的情況, 只有簡單的變數, 方便理解布局的概況, 現在舉一種有array的情況的stack, 假設funcTest()中定義了int array[3], 則布局如下:
        * ```
		  高位地址
		  ------------
		  | funcTest的堆疊幀 |
		  | 返回地址:
		  | 幀指標        |
		  | testArr =     | testArr[3]
		  | testArr =     | testArr[2]
		  | testArr =     | testArr[1]
		  | testArr =     | testArr[0]
		  | result       | <- 局部變數 result
		  ------------
		  低位地址
          ```
        * 可以看到array在stack中是由"低位址->高位址增長", 原本這是合理且直觀的設計, 你在c語言中使用array要取下一個陣列元素的值的時候只要直接往後推移一個單位的地址即可, 不過這樣的設計就是導致overflow攻擊的關鍵了, 因為當你超過陣列宣告範圍, 例如將testArr[4]指定值得時候, 記憶體位址其實是貞指標的位址(仔細看上面的布局), 而testArr[5]指定值得時候, 記憶體地址其實是函數返回的地址. 
    * 如何利用覆蓋函數返回地址形成攻擊?
      * 要說清楚這件事情, 必須先建立一個概念, **記憶體內所有資料全部都是二進制機械碼**, 一個Process內的stack, heap, data, text全部都是存放二進制機械碼, 由低位址到高位址一個個說明:
        * **text**: 儲存程式的機械碼（Code），包括函式、方法和整個程序邏輯。
        * **data**: 儲存程式的初始化資料（Initialized Data），例如全域變數、靜態變數等。
        * **heap**: 儲存動態配置的資料（Dynamic Memory），例如使用 malloc() 或 new 配置的記憶體。
        * **stack**: 儲存函式的呼叫堆疊（Call Stack），包括函式的參數、局部變數和返回地址。
		* 以上這四段, 都是由"CPU的機械碼指令(例如mov, add, jmp等)"以及"資料(整數, 字串等等的二進制機械碼型式)"組成(事實上所有電腦數據只要進入記憶體了, 則必定是將要交給CPU, 則必定是此形式). 
        * stack是動態增長的, 但要注意的是, stack本身只會存函數的返回地址, 參數, 變數, 而沒有函數本身的邏輯代碼, 這些邏輯代碼都在text裡面, 當程式需要執行一個函式時，會將函式的機械碼從 Text 段載入到 CPU 的指令緩衝區（Instruction Cache）中，然後執行。所以嚴格來說函數的邏輯代碼都在text裡面(這也是為何c語言只需要header就能編譯, 而不須函數定義檔). 而stack中函數的"返回地址"其實就是指向text段中某段對應的記憶體位置, 在函數結束後, 讓程序處理接下來的代碼任務. 整個過程概述如下:
          * step_1. 函數被呼叫，返回地址被push進 Stack 中。
		  * step_2. 函數執行完成，返回地址被pop出 Stack 。
		  * step_3. 返回地址被載入到 IP/PC 寄存器中。
		  * step_4. CPU 跳轉到 Text 段中該地址的指令，繼續執行接下來的代碼。
        * 簡而言之, 可以把stack想像成text的資料暫存區, 這也是為何stack的位址從最高位開頭開始, 因為stack的地址的開頭必須要確定(固定), 不能變來變去, 才能讓text抓到. 
        * 而我們上面提到, 當函數執行完成後, 會將返回地址pop出, 並跳轉到返回地址指向的地址繼續執行邏輯代碼, 而返回地址本來指向text段中接續的程序邏輯代碼, 但如果你用buffer overflow的方式把返回地址改寫了, 程序本身根本不會知道現在返回的地址不是在正確地方, 他就只是繼續執行邏輯代碼. 如果這個時候返回地址指向惡意的邏輯代碼地址, 攻擊就成功. 
        * 需要注意的是, 只有在函數結束時, 才會使用返回地址, 跳轉回text的接續位置, 也就是說其實Buffer overflow將返回地址覆蓋後, 錯誤不會馬上發生, 而是等到函數結束時, 跳轉後才發生. 
        * 而攻擊者無法直接在text中插入惡意代碼, 因為text是事先編譯好的, 無法動, 唯一能夠插入惡意代碼的記憶體區域就是stack(以及heap), 這些可以透過"輸入"來插入值的記憶體, 因為對程序來說stack, heap, text, data其實就是一樣形式的記憶體, 只是位址不同罷了, 程序不會去管現在到底執行stack, heap還是text或data, 也不會去管text的資料是在stack或是heap中或是其他地方, 他只管照著執行, 這些stack, heap, text, data分段都是程序初始化時, 作業系統建立的. 
        * 總之最直接的做法, 就是在輸入buffer的值的時候, 把惡意代碼直接放在buffer中, 例如buffer[100], 其中buffer[0]~buffer[20]是正常數據, buffer[21]~buffer[99]則是惡意代碼. 然後我們讓返回地址複寫成條轉到buffer[21]的位址, 由於buffer[21]~buffer[99]是連續的, 程序不會去管現在的位址在哪(有個不是很精確卻很好理解的說法是, 程序會以為自己跳轉到了text中), 他會接著執行buffer[21]~buffer[99]的程序邏輯.        * 我們知道text中存的就是一大串CPU機械碼指令, 如果我們可以把buffer[21]~buffer[99]變成執行惡意行為的機械碼指令, 就算攻擊成功了. 
        * 由於攻擊者無法精準知道buffer的位址, 所以實際輸入buffer的內容可能是以下: [NOP, NOP, NOP, NOP,...] + [shellcode] + [惡意地址, 惡意地址, 惡意地址,...], shellcode是惡意代碼的機械碼, NOP是"no operation"指令, 甚麼動作都不會做, 讓CPU空跑, 然後跳到下一個指令. 這個NOP是CPU的特殊指令, 本來是用來矯正和延遲的作用, 但是在此用來攻擊. 由於不曉得buffer的開頭地址在哪, 藉由填充NOP, 可以達到增加執行到shellcode的概率, 而我們我們也不曉得返回地址的地址在哪, 所以在buffer的後面填充多個惡意地址增加概率. 
    * 以上所述, 是最簡單的實作, 實際上這種程度攻擊已經很難成功了. 在古早時代, stack要馬在特定地址, 要馬就是在某些常見的特定地址. 但現在作業系統都有機制應付, 例如"non-executable stack", "address-space randomization", 這些技術都讓簡單的攻擊失效. 需要更高階的技巧. 
    * 可參考以下: 
	  * [reference_1](https://www.reddit.com/r/C_Programming/comments/1f42kpg/how_do_i_exploit_a_buffer_overflow_vulnerability/)
	  * [reference_2](https://www.coengoedegebure.com/buffer-overflow-attacks-explained/)
  * ## 29B. memory leak, 
    * memory leak其實就是動態記憶體(heap)沒有釋放, 類似的狀況如果接二連三發生, 會導致到後來發現作業系統發現可用記憶體越來越少(都沒釋放, 所以被占用), 到了無可使用的地步, 記憶體洩漏發生在一個程序動態分配內存後，由於程式邏輯錯誤或其他原因沒有正確釋放這些內存，導致這些內存無法再被該程序或其他程序使用。隨著時間的推移，這些未釋放的內存會積累，最終可能會耗盡作業系統的可用內存，影響整個系統的性能和穩定性。
  * ## 29C. stack overflow, 
    * 當程序試圖使用超過堆疊限制的內存時會發生. 通常是由於遞歸(recursive, 自己呼叫自己)函數沒有正確終止或無限遞歸導致的. 最簡單的例子就是建立一個"沒有終止條件的recursive函數", 這樣每次呼叫函數, 都會在stack建立一個stack frame, 永無終止, 而stack通常有大小限制(依環境或作業系統設定), 幾MB左右為上限(這也是程序在處理大的檔案或數據時必須使用heap的原因, heap的上限比stack大很多), 這導致stack超過大小限制, 一般作業系統此時都會介入, 但在沒有任何保護機制的環境時, 是會有覆蓋數據的情況發生的(跟buffer overflow類似的覆蓋).

  * ## 29D. 常見的hacking 練習網站:
    * pwnable.tw 
    * hack the box

# Chapter_30. 如何對segmentation fault進行debug?(編譯器如果麼有告訴你哪一段代碼segmentation fault)??



# 額外筆記:
  * ## 1. 
    * ```c
	  // 只要有一個不為0則執行
	  if (testVar1 != 0 || testVar2 != 0)
	  // 兩個都不為0則執行
	  if (testVar1 != 0 && testVar2 != 0)
	  you can use truth value table to clcear this idea.
      ```

  * ## 2.
    * [reference](https://www.quora.com/Does-static-memory-allocation-work-without-an-OS-in-embedded-systems)
