# Chapter_1. Linux的基本原則
  * Everything is file
  * 這是unix及linux的設計哲學, 與所有作業系統一樣, "執行文件"全部存放在硬碟, 開機的時候由bios和bootloader, 將這些kernel的"執行文件"載入到記憶體, 之後將控制權交給內核. 
  * 有些電腦儲存空間有限, 例如embedded system, 他們的硬碟空間有限, 只能使用閹割版的linux, 例如最常使用的embedded system 是embedded linux Yotco. 
  * 而手機及行動裝置使用的系統其實也是embedded system, 例如android其實也是embedded system(雖然它的功能比一般低階的embedded system要強的多)
  * 所謂embedded system通常是指專為特定任務設計用於執行特定任務, 且資源有限, 需即時響應, 用以集成更到更大的系統, 例如印表機, 洗衣機, 一些只能家電, 或是工業用機器人, 通常沒有傳統硬碟來存放作業系統, 而是使用flash memory(快閃, 也就是隨身碟or SD卡使用的記憶體, 有些可插拔有些是內嵌在電路板上)來存放作業系統. 
  * 而一般計算機則是通用設計為目的, 可執行多種任務, 資源豐富. (要學習embedded system, 可查詢看看qemu或是yotco)

# Chapter_2. Linux根目錄的幾個重要文件(目錄):
  * ## 2A. **/usr**
    * "unix system resource"的縮寫, 大部分系統自帶的"可執行文件(以及你後來自行安裝的可執行文件)", 庫文件、共享數據和常用指令(算可執行文件), 都位於這個目錄下, 包含各種常用指令. 
    * 需要注意的是/usr裡面的東西都是"系統層級"的東西, 也就是說它是面向所有使用者的
    * 以下是/usr內的重要文件:
      * **/usr/bin**, 絕大部分的系統自帶的可執行文件, 以及你使用apt或是其他軟件管理包安裝的工具的可執行文件, 都在這裡, 例如你使用"apt install vim", 其實就是把vim的可執行文件從網路上下載並存放在"/usr/bin"中, 而"/usr/bin"本身就在$path中了, 所以你可以直接使用該執行文件. 同樣的你如果把"/usr/bin"從$path中移除了, 你將無法執行大部分的操作, 例如cd, mv, cp, ls等等. 不過大部分修改path會使用export, 這個不是永久指令, export PATH方式只對當前會話有效，一旦退出當前終端會話，修改會失效, 這便是為了以防萬一. 倘若真的不小修改$path, 把/usr/bin移除了, 也可以使用全路徑調用命令, 例如使用/usr/bin/ls調用"ls". 順帶一提, 大部分安裝的可執行文件只有可行文件, 要知道源代碼需自行去github看.
      * **/usr/sbin**, 存放系統管理命令和應用程序，通常需要超級用戶（root）權限來執行。示例命令：fsck, ifconfig, iptables. 通常你使用一個指令, 他如果要求你要用sudo, 就是表示他是在/usr/sbin中
      * **/usr/lib**, 即可執行文件庫存放區, 這些庫文件為**/usr/bin**以及其他目錄中的可執行文件提供必要的函數和功能，以便它們能夠正確運行。 簡單來說, 一個可執行文件(程序), 或多或少會使用到共通的庫, 例如/usr/bin中的ls於cp可能都使用到了XX功能, 類似的狀況很多, 所以lib實際就是這些共通函數或者模組或插件的集中處, 有分靜態庫(.a檔案)和動態庫(.so檔案, 即share object). 注意, 他們都是可執行文件(程序), 也就是bin檔案, 只是通常只有函數功能, 沒有完整的執行能力. 靜態.a檔案在某程序A需要使用的時候會將其加入到A程序中, 而動態.so檔案則是在假設B程序需要時動態與B程序相互合作, windows上也有對應功能文件(或說檔案), 就是有名的dll檔案, 與.so檔案對應.
      * **/usr/local**, 這個目錄通常用來存放在系統安裝之後手動編譯和安裝的應用程序和庫。這些文件通常不會被系統包管理器管理. 也就是說如果你不是使用apt(或其他系統包管理工具)安裝的, 例如有些東西使用npm安裝, 他就會把文件存放到此。而其子目錄基本仿照/usr的內容, 如/usr/local/bin, /usr/local/sbin, /usr/local/lib
      * **/usr/share**, 要徹底了解這個目錄, 我們必須先了解linux的多人模式如何運作. 很久以前, 個人電腦尚未普及時, 一個公司或團隊, 通常只有一台主機, 團隊的每個人使用各自的終端機連線至該主機進行操作. 為了區分每個使用者, 以及限定每個使用者的權限, linux採用的是"使用者對文件的操作"權限設定, root擁有絕對權限, 能做任何事情, 所有使用者都要由root創建. 要進入一個目錄必須要有該目錄的執行權限(就是inode中的x必須要有). 如果你沒有該目錄的執行權限, 那理論上你連該目錄的子目錄都無法進入, 即使你擁有該子目錄的權限, 也就是說假設你要進入dir/subdir, 你必須要有dir的執行權限, 不然即使擁有subdir的執行權限, 你也進不去dir/subdir, 除非你本來就在dir裡面, 這個時候可以使用相對路徑cd subdir. 這裡有一個[參考討論](https://unix.stackexchange.com/questions/13858/do-the-parent-directorys-permissions-matter-when-accessing-a-subdirectory). 理論上使用者bob的home目錄在/home/bob裡面, 且只有bob以及root可以進入. 當創建一個新用戶時(bob的基本帳戶設置存放在/etc/passwd)，，默認會設置家目錄的權限為 700, 這意味擁有者（bob）擁有讀取、寫入和執行權限（rwx）。同群組的用戶和其他用戶：無權限（無讀取、寫入和執行權限）, 當然這些都可以由root修改, 只要root想要可以讓alice進入/home/bob. 而/usr/share的功用就是有一個默認folder是讓所有使用者共享"系統層級"的靜態文件, 例如代碼, txt, 圖片文件等等. 再次強調, /usr裡面的東西都是"系統層級", 假設bob使用apt install something, apt會把可執行文件裝入/usr/bin, 靜態文件裝入/usr/share. 也就說apt本身是"系統層級"的安裝管理, 他是為系統服務, 不是為特定使用者, 這也是為何我們使用apt時, 系統會要求要有root權限, 你必須使用sudo. 如果bob想要安裝自己個人的執行應用, 應該在/home/bob裡面設置一個bin之類的folder, 將執行文件下載至其中執行, 這樣這個應用就不是"系統層級". 而是只給bob. 也就是只有/home/bob裡面的東西是專門給bob服務的(當然root也有完整的權限)
      * **/usr/include**, 這個文件夾存放都是c語言的.h檔案, 雖然我們知道linux本身是由c語言寫成, 但這個目錄與linux運行本身沒有任何關係, 他是純粹為開發者所設置的目錄, 其中包含大量的.h文件, 例如stdio.h, stdlib.h, 這些都是c和c++開發應用時必用的文件, 當你在用gcc編譯.c檔案時, #include <stdio.h>會自動去/usr/include尋找, < >其實就是/usr/include的shortcut. 這時候有個問題, .h文件只有宣告函數, 而沒有定義函數, 定義函數的文件在哪??其實定義函數的文件都放在/usr/lib裡面的可執行文件(當然都是編譯過後的, 想要源代碼自行去github), 尤其是"/usr/lib/x86_64-linux-gnu/libc.so"動態庫,  他包含了stdio.h, stdlib.h, string.h, math.h, time.h, error.h的對應函數定義執行文件(當然都是編譯好的). 你如果再linux寫了一個簡單的hello. 假設程序使用#include <XXXXX.h> 他會自動去/usr/include中尋找.h文件, 然後自動去/usr/lib尋找.h文件對應的函數定義編譯後可執行文件(如果是stdio.h, 則其包含在/usr/lib/x86_64-linux-gnu/libc.so). 而如果使用#include OOOOO.h, 則是會把OOOOO.h對應的定義文件(可能是你自己寫的XXX.c文件)編譯後加入最終結果out文件. 也就是說假設你寫了一個func.h文件, 然後寫一個對應的func.c, 然後編譯, 結果為out.o, out.o會包含func.c編譯後的執行文建內容. 假設你寫一個#include <stdio.h> printf("hello, world\n"); 然後編譯成執行文件out.o, 再把out.o放在一個沒有libc.so文件的主機裡, out.o是無法運行的, 因為找不到printf 函數的實現. 在多說一點, libc.so可不是只有開發會用到, 事實上由於Linux本身是由c編寫的, 他的很多常用指令都用到了c的標準庫(編譯後, 也就是libc.so), 也就是說我們常用的很多指令例如"ls", "mv", "cp", "cd"等等很多都依賴於libc.so動態庫. 所以你如果把libc.so改名或是移動了, ls, mv, cp, cd非常多指令找不到依賴, 就全部不能用了, 這裡有個[實際案例](https://stackoverflow.com/questions/39885343/cannot-run-any-commands-because-i-moved-the-libc-so-file). 至於可執行程序與所需的動態庫.so文件的連結, 是由ld.so負責(通常位於/usr/lib或相關文件中, 可以使用ldd /bin/ls查看ls所的依賴順便看到ld.so的路徑), ld.so默認會在/usr/lib尋找依賴. 有個問題是/usr/lib有大量庫, ld.so豈不耗時? 這是由於ldconfig會建立ld.so.cache, 是二進檔案且通過特殊的算法和資料結構(例如甚麼哈希或索引樹), ld.so使用ld.so.cache速度比遍歷/usr/lib快得多.  當然最快的方式是直接在程序文件指定依賴庫路徑, 例如(假設)ls文件中使用rpath(編譯時指定, 寫死的)或是runpath(運行時指定, 但可能能有安全風險, 例如運行時輸入特定代碼用以觸發特定bug)設置為/usr/lib/libc.so. 只是如果路徑指定死, 庫文件只要移動位置可能就無法使用(這我可以理解, 但是copilot說庫版本更新會需要可執行文件重新編譯? 這是怎麼回事? 如果庫版本更新的內容多到會需要使可執行文件重新編譯, ld.so.cache會需要可執行文件重新編譯啊? ld.so.cache只是把所以庫文件的名稱和路徑整理起來, 用較為高效的方法和數據結構運行, 他不能解決可執行文件本身內容對庫版本的需求吧?)
  * ## 2B. **/etc**, 
    * 它的名稱來自於最早期 UNIX 系統中的 "et cetera", 另一種說法他是"editable text configuration". 裡面大部分存放"系統層級"相關的配置文件(也就是config文件)或腳本, 都是純文字文件居多, 包含你安裝系統層級應用的時候, 配置文件也會在此. 例如你安裝nginx, 則配置應該會在/etc/nginx/nginx.conf, 你安apt安裝的vim, 他的config會在/etc/vim/vimrc(當然vim特定使用者可以在自己的目錄設置vimrc, 例如/home/user_name/vimrc, vim的設計會優先考量), 較為基本的如下:
      * 用戶相關配置文件:
        * **/etc/passwd**: 存放用戶賬戶信息的純文字檔案, 也包含各種進程帳戶(例如甚麼systemd-network, syslog之類的), 他的標準格式大致如->sara:x:1000:1000:Sara Z:/home/sara:/bin/bash, 使用":"對作為間隔, 其代表的意思為sara(username):x(帳戶密碼, 存放在/etc/shadow):1000(user id):1000(group id):Sara Z(GECOS):/home/sara(使用者家目錄):/bin/bash(使用者預設shell). /etc/passwd是系統對"使用者名稱", "使用者ID", "使用者群ID", "使用者家目錄", "使用者預設shell", 的唯一依賴, 你如果修改了是會生效的. 例如sara:x:1000:1000:Sara Z:/home/sara:/bin/bash改成sara:x:1000:1000:Sara Z:/home/sara:/bin/zsh, sara下次啟動系統時, 就會自動使用zsh. 他有點像是資料庫裡存放著各種用戶的帳戶資訊, 包含帳號密碼, 這些都是系統的直接依賴, 你的修改都是有效的.
        * **/etc/group**: 存放組信息
        * **/etc/shadow**: 存放用戶密碼及相關安全信息
        * 需要注意的是, 修改用戶配置文件, 不等於修改用戶對某文件的access權限, 因為文件的獲取權限設定是存在"inode(index node)"裡面, 而inode本身是文件系統的一部份, 跟這裡提到的配置略有關係但不是一回事.
      * 服務和守護進程配置
        * **/etc/int.d/**: 存放系統啟動和關閉時執行的服務腳本
		* **/etc/systemd/**: 使用 systemd 的系統，其服務和守護進程配置存放在這裡
	  * 網路配置
		* **/etc/hostname**: 系統主機名配置文件
		* **/etc/hosts**: 本地主機名解析文件, 相當於"本地DNS", 可以將domain name映射到IP地址, 例如192.168.1.10 example.com, 在 DNS 服務器不可用或用於快速本地測試時, 會派上用場.
		* **/etc/networks**: 存放網絡設置和接口配置文件
		* **/etc/iptables**: 存放過濾網路封包的規則文件(修改後, 重新加載內存, 或重新啟動系統後生效), 他算是最原生的linux 防火牆系統
      * 設備和資源配置
		* **/etc/fstab**: 文件系統掛載點配置文件
		* **/etc/mtab**: 當前掛載的文件系統信息
      * 程序和應用配置
		* **/etc/apt/**: APT 包管理工具的配置文件（適用於 Debian 和 Ubuntu 等）
		* **/etc/yum.conf**: YUM 包管理工具的配置文件（適用於 Red Hat 和 CentOS 等）

  * ## 2C. **/home**
    * 存放用戶的個人主目錄，每個用戶在這裡都有自己的目錄，如 /home/user_name。這是用戶存放個人文件和設置的地方。

  * ## 2D. **/dev**
    * 不是"development", 而是"devices"的意思, 存放"硬件設備"及"虛擬設備(pesudo device)"有關的文件.
    * 在linux文件系統中, 每個硬件設備實體被表示為一個文件. 例如硬盤被表示為/dev/sda, 終端設備可能被表示為/tty1, 系統程序可以直接和這些設備文件互動. 例如讀取硬盤可以使用以下命令: dd if=/dev/sda of=/path/to/output/file bs=512 count=1, 表示將硬盤/dev/sda讀取第一個512字節並寫入到指定文件中. 或是寫入數據到/dev/null: echo "Hello, World!" > /dev/null.  
    * 需要注意的是, /dev存放的都是"可文件化"的設備, 可文件化的設備主要都是"靜態設備(可讀寫, 數據永存)", 包含"儲存設備", 例如硬盤(/dev/sda, /dev/sda1硬盤分區), 光驅(/dev/sr0), 字符設備, 例如終端(/dev/tty), 虛擬設備(/dev/null, /dev/zero, /dev/random), 音頻設備(聲卡和音頻輸出/輸入設備, 例如/dev/snd/pcmC0D0p), 網路設備(/dev/net/tun, 即虛擬網路接口), 輸入設備(如鍵盤滑鼠, /dev/input, /dev/input/mouse0). "動態設備(不可讀寫, 數據不永存, 且更新頻率極高)", 靜態設備和動態設備的區別可以簡單想成, 靜態設備是"被處理者", 而動態設備則是"處理者". 動態設備, 例如CPU, 內存, 通常難以文件化, 他們會採用"虛擬文件"的形式存在, 不會放在/dev裡面.

  * ## 2E. **/proc**(是一虛擬文件)
    * 即"進程(process)"的縮寫, 是個虛擬目錄, 提供系統運行時的動態信息，主要用來查看內核數據結構和系統進程的信息, 是內核(kernel)動態生成的, 並不存在於任何儲存裝置上。通過"虛擬文件"和"虛擬目錄"的形式展示內核和進程的狀態。同時也包含CPU及內存的狀態.
    * 這裡的虛擬文件也是一種"動態文件(數據會時間變化, 你每次打開可能都不盡相同)". 
    * 虛擬文件不是真的文件, 並沒有"文件系統", 他故意設計成文件系統的模樣, 方便使用者閱讀和操作. 
    * /proc內的虛擬文件大部分都是純文字文件, 單純用來顯示即時的進程資訊(大多數只讀), 內核生成後放置在內存上, 也就是說/proc是直接放在內存, 而不是硬碟! 當你用任何editor(文字編輯器)去修改其內容後想要儲存, 會出現錯誤, 因為editor無法對不在儲存裝置(硬碟)上的文件進行修改, 想要修改必需透過特殊接口.
	
  * ## 2F. **/sys**(也是一虛擬文件) 
    * 即"system"縮寫, 同樣是虛擬目錄, 他是提供內核(kernel)運行時的動態訊息, 他跟/proc很像, 我有查到一段說明:
      * Essentially /proc and /sys are the same. sysfs was added in kernel 2.5 or 2.6 due to clutter in procfs. The procfs was only meant to hold process information. eventually everything started getting mixed into proc and it created a twisty maze with device data stuck in different spots all over the place. Meanwhile, sysfs was implemented with the objective of segmenting device data from procfs. Specifically, /sys maintains more detailed (position of nodes actually represents the device hierarchy by subsystem) device process information. For each object in the driver model, a directory is created. The device file structure being:
        * **/sys/devices**: devices by physical layout
        * **/sys/bus**: symbolic links to devices
		* **/sys/block**: devices by block
		* **/sys/class**: devices by class
      * On your local system you might find man page at man sysfs and information about modifying kernel parameters in /proc/sys with man sysctl. 
      [Here's the source explanation talks about this](https://serverfault.com/questions/65261/linux-proc-sys-kernel-vs-sys-kernel)

# Chapter_3. Linux檔案系統(file system), ext4, inode
  * ## 3A. inode
  * ## 3B. ext4 

# Chapter_4. 記憶體管理機制(即是虛擬記憶體機制, 部分額外的重要內容可以參考c語言筆記的freestanding筆記)
  * ## 3A. **內存碎片** 
    * 是記憶體管理機制為了解決的重要問題之一, 指的是無法被利用的內存, 可以分為"外部碎片"和"內部碎片"([reference](https://www.nowcoder.com/discuss/544284985797169152))
      * **外部碎片**: 由於任何應用在申請記憶體時, 都需要連續的記憶體, 所以可能會有類似以下的狀況, 假設總共有16MB的實體內存, 而整條記憶體使用狀況為|未使用(1MB)|A應用(6MB)|未使用(2BM)|B應用(3MB)|未使用(1MB)|C應用(3MB)|, 假設此時D應用想申請3MB的內存, 總空間剩餘的內存是滿足需求的, 但是每一快空閒內存卻都不滿足.
      * **內部碎片**: 為了解決外部碎片的問題, 一種簡單的方式就是把記憶體切單位塊, 例如3MB為一個單位塊, 每次分配最少分配到一個塊, 例如A應用需6MB則分其2塊, B應用需3MB則分一塊, 但這樣有個問題, 就是假設D應用只需1MB, 卻也分給他一塊(3MB), 則多出的2MB稱之為"內部碎片", 這其實就是"你的應用所需的記憶體總長度很難剛好整除單位塊大小導致的.
  * ## 3B. 管理機制
    * 一般作業系統為了更有效的運用記憶體, 引入了虛擬記憶體機制, 分為segment或page, 
      * **segment**(對應"外部碎片")的是給一個應用一個剛好且真實的連續物理地址, 並將起始地址記為"基地址", 並記錄他的區間長度範圍(成為segment邊界長度), segment內部的沒一個記憶體, 都有自己的"segment 偏移"(其實就是相對於起始地址的位置, 例如起始地址在segment內部來看, 其segment偏移就是0, 往下一個記憶體偏移就是1...以此類推), segment透過把起始位址加上偏移得出線性地址(在沒有其他額外機制的情況下這個線性地址就是真實地址了), segment內部的虛擬記憶體從何開始其實沒麼重要, 只要知道他必定連續即可, 但是會產生外部碎片.
      * **page**(對應"內部碎片", linux採用), linux內核選擇採用pages(頁) and page tables(頁表)來實現虛擬記憶體, 其實就是上面所述的"虛擬記憶體單位塊(內部是連續的虛擬地址)", 他map到一段真實連續的實體記憶體塊, 假設某應用可能使用了page1, page2, page3, 這page1, page2, page3是連續的(應用需要使用連續記憶體), 但是對應的物理實體記憶體塊不一定能連續(例如分別對應block4, block7, block8). 為了儘量減少內部碎片, Linux有其他機制, 例如buddy分配器
        * **page tables**: 記憶了所有虛擬記憶體的對應實體記憶體位址, 他本身也存放在內存. 
        * **page**: 具有固定大小的內存管理單位。大多數系統使用的頁面大小是4KB，但也有其他常見的大小，例如2MB和1GB（這些通常稱為大頁（large pages）或巨頁（huge pages.)
    * 一個**process**容納一個程序, 他的記憶體使用布局稱為"process memory", 通常會有許多pages組成, 一個page只專屬於一個process. 每個page都map到一個實體的連續記憶體block
	  * Process的**定址空間**(重要) 
        * 所謂的定址空間指的是process虛擬記憶體的虛擬地址的開頭到結束所涵蓋的連續地址範圍, 32-bit經典模式的地址空間是從0xFFFFFFFF~0x00000000, 總共4GB(這只是定址空間, 拿來定址用的, 不是真的佔用, 別誤會). 
        * 這個定址空間內部又再劃分成**OS kernel space(內核空間)**及**User mode space(使用者模式空間)**, 
          * **OS kernel space**定址: 從0xFFFFFFFF~0xC0000000共1GB
            * kernal space劃分為|直接map所有物理page|VMALLOC|持久mapping|高端mapping|, 
          * **User mode space**從0xBFFFFFFF~0x00000000共3GB.[reference](https://www.ptt.cc/bbs/C_and_CPP/M.1472449011.A.2A3.html), [reference_2](https://unix.stackexchange.com/questions/509607/how-a-64-bit-process-virtual-address-space-is-divided-in-linux), [reference_3](https://cg2010studio.com/2011/06/26/process-in-memory/)
            * 一個Process中的user mode space又可在劃分成|高位址|stack|->未被占用的定址空間<-|heap||data(global variable)||text(code)|最低位址|. 
              * 可以看到stack從高位址向下增長, 他是動態的, 包含宣告的變數, 函數, 按照資料結構stack進行縮放(雖然一個函數及變數本身占用的大小是靜態的, 但是程序運作時本來就會時常宣告然後湮滅函數或變數, 所以stack增減是本來就是如此), 而Heap增長方向與stack相反, 程序運行時呼叫sys_call來改變變數大小, 也是動態增長, 而data及text則固定大小(也必須固定大小, 不然heap的最底層位址會被迫移動),
              * 注意, "未被占用的定址空間"就只是定址空間而已, 所以雖然"user mode space"定址空間有3GB, 但實際上真正佔用的記憶體不會計算"未被占用的定址空間". 所以其實process的記憶體占用大小是動態變化的! 這符合記憶體的管理上想要盡量不良費的原則.
        * 這兩種模式其實與CPU權限有關.  在 x86 CPU 的保護模式底下，根據處理器權限的不同，又可區分為 Ring 0, 1, 2, 3 等 4 種權限等級。Ring 0 的權限最大，可以直接存取所有硬體；而 Ring 3 的權限最小，沒有任何硬體權限。處理器權限的設計，主要是為了增強容錯的能力。譬如在意外錯誤發生時保護資料內容，或保護系統不被惡意的軟體侵害。對應於作業系統與應用軟體，作業系統的核心 (kernel) 是運行在 Ring 0 的權限下，Ring 1, 2 則都給驅動程式使用，應用程式則運行在 Ring 3。相對作業系統來說，則是簡單分成 kernel mode 與 user mode。在 kernel mode 下執行的是可以存取硬體支援的指令動作，而在 user mode 底下的程式，則是只能透過作業系統所提供的系統呼叫常式 (system call)，切換到 kernel mode 下取得資源。 
		* 結論: 簡單來說一個process的記憶體模式若為使用者模式, 則他會有stack, heap, segment. 而stack, heap, segment各自都會有數個page組成. kernel模式也是類似狀況, 可以把page當成是linux記憶體管理的最小單元. [reference_1](https://hackmd.io/@sysprog/linux-memory), [reference_2](https://ithelp.ithome.com.tw/m/articles/10158922)

# Chapter_5. process和thread的解釋
  * 所謂的program, 即程序, 它是完成一個運算任務(可以很複雜)的實現邏輯, 我們將其用"程序語言"寫出, 然後編譯後成了一系列CPU機械碼指令, 存入內存後, 批次丟給CPU運算, 最終解決這個program所要完成的運算"任務". 最早的作業系統便是為了解決"多任務並行"的問題而誕生. 作業系統誕生之前, 所有電腦都是embedded system, 只能運行一隻program, 任何program本身都占用硬件的所有資源和實體記憶體(請參考c語言筆記的freestanding以及embedded system筆記), 為了讓一台電腦能實現多任務並行, 人們寫了一個超級大的程序叫做"作業系統", 他是一隻管理program的program, 作業系統主要的任務(之一)就是使用虛擬內存的內存管理邏輯, 創造出"Process"作為一個program機械碼運行的虛擬記憶體空間載體, 也就是說一個process乘載著一個Program, 從物理層面來說, 一個process的虛擬記憶體乘載著一個program的機械碼, program在process中能使用的資源即是作業系統分配給process的. 如今電腦依舊只執行一個Program, 即作業系統, 只是這支超級program, 它使用虛擬化的技術, 乘載著許多虛擬program, 而虛擬program們也依舊像是古早embeded system的時候運行, 只是這下它們各自只占用了一個process的虛擬資源(虛擬記憶體), 並且能從作業系統申請其額外的輔助功能(system call), 作業系統接著讓不同process之間以"多時分工"的方式使用cpu(就是一小段時間給A程序, 接著一小段時間給B程序, 如此往復, 製造出並行的感覺), 但隨著各種程序的設計越來越複雜, 人們發現, 一個程序當中也有許多任務需要並行處理, 於是就誕生了thread, 實際上就是大任務(process)中的小任務(thread), 但要注意的是小任務隸屬於大任務, 但大任務本身不隸屬於任何東西, 他就是一個獨立的任務. thread本身是為了所隸屬的process而服務, 他是為了完成process而存在的, 一個process內的threads都是為了該process服務, 但是一個作業系統裡面的process都是互相獨立的, 是為了完成自己而存在. 作業系統合理地設計讓threads可以共享其隸屬process的資源, 這是合理且有效率的設計, 任何process都至少有一個thread. [reference_1](https://www.reddit.com/r/explainlikeimfive/comments/35qw88/eli5_what_is_a_thread_in_a_processor/)

# Chapter_6. system call
