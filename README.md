# SortingVisualizer
This is a visualization tool for various sorting algorithms
 - BubbleSort
 - SelectionSort
 - MergeSort
 - QuickSort
 - HeapSort



PROJE TANITIMI
Projemiz Selection Sort, Buble Sort, Insertion Sort, Merge Sort ve Quick Sort sıralama algoritmalarını kullanarak Scatter, Bar ve Stem grafik çeşitleri içerisinde kullanıcıya değer aralığını seçtiği grafiğini sunmayı amaçlıyor. Bu sıralama algoritmalarını kısaca tanıtmak gerekirse;
 
Selection Sort
Selection sort çalışma mantığı olarak listedeki en küçük elemanı bulup,  en küçük sayıyla baştaki sayıyı yer değiştirir. Daha sonra tekrar en küçük sayıyı arar ancak bu sefer en başa attığı sayıya bakmaz yani 2. elemandan (1. indexten ) itibaren aramaya başlar. Bu şekilde diziyi sıralı hale getirir.
Buble Sort
•	    Kabarcık Sıralaması, bilgisayar birimlerinde kullanılan yalın bir sıralama algoritmasıdır. Sıralanacak dizinin üzerinde sürekli ilerlerken her defasında iki öğenin birbiriyle karşılaştırılıp, karşılaştırılan öğelerin yanlış sırada olmaları durumunda yerlerinin değiştirilmesi mantığına dayanır. Algoritma, herhangi bir değişiklik yapılmayıncaya kadar dizinin başına dönerek kendisini yineler. Adına "Kabarcık" sıralaması denmesinin nedeni büyük olan sayıların aynı suyun altındaki bir kabarcık gibi dizinin üstüne doğru ilerlemesidir.
•	Başlangıçta yer yer değiştirme sıralaması olarak adlandırılan kabarcık sıralaması, dizi içindeki büyükelemanların algoritmanın her adımında dizinin sonuna doğru doğrusal olarak ilerlemesini sağlar. Bu ilerleme, seçmeli sıralama algoritmasındaki dizideki değeri küçük olan elemanların dizinin başında kümelenmesi yöntemine benzer şekilde gerçekleşir.
Insertion Sort 
     Eklemeli Sıralama bilgisayar bilimlerinde kullanılan ve sıralı diziyi her adımda öğe öğe oluşturan bir sıralama algoritmasıdır. Büyük dizilerle çalışıldığında hızlı sıralama, birleştirmeli sıralama ve yığın sıralaması gibi daha gelişmiş sıralama algoritmalardan daha verimsiz çalışır. Ancak buna karşın bazı artıları da vardır:
•	Uygulaması kolaydır.
•	Küçük Veri kümeleri üzerinde kullanıldığında verimlidir.
•	Çoğunluğu zaten sıralanmış olan diziler üzerinde kullanıldığında verimlidir.
•	Karmaşıklığı olan seçmeli sıralama ve kabarcık sıralaması gibi çoğu yalın sıralama algoritmalarından daha verimlidir.
•	Kararlı bir sıralama algoritmasıdır (değeri eşit olan öğelerin asıl listedeki göreceli konumlarını değiştirmez)
•	Sıralanacak diziyi yerinde sıralar, ek bir bellek alanı gerektirmez.
•	Sıralanacak dizinin hepsinin algoritmanın girdisi olmasına gerek yoktur. Dizi parça parça da alınabilir ve sıralama işlemi sırasında diziye yeni veriler eklenebilir.
İnsanlar herhangi bir şeyi (örneğin, iskambil kartları) sıralarken, çoğu durumda eklemeli sıralamaya benzer bir yöntem kullanırlar.
Merge Sort
     Merge Sort (Birleştirme Sıralaması), diziyi ardışık olarak en küçük alt dizilerine kadar yarılayan sonra da onları sıraya koyarak bireştiren özyineli bir algoritmadır. Yarılama işlemi en büyük alt dizi en çok iki öğeli olana kadar sürer. Sonra "Merge (Birleştirme)" işlemiyle altdiziler ikişer ikişer bölünüş sırasıyla sıralı olarak bir üst dizide bireşir. Süreç sonunda en üstte sıralı diziye ulaşılır.
Quick Sort
     Hızlı sıralama, günümüzde yaygın olarak kullanılan bir sıralama algoritmasıdır. Hızlı sıralama algoritması n adet sayıyı, ortalama bir durumda,karmaşıklığıyla, en kötü durumda ise karmaşıklığıyla sıralarAlgoritmanın karmaşıklığı aynı zamanda yapılan karşılaştırma sayısına eşittir.


   Bu sıralamalardan sonra kullanıcıya grafik çeşitlerinden, Scatter, Bar ve Stem grafikleri sunulmaktadır. Kısaca bu grafik türlerini açıklıcak olursak;

A.	Scatter
  Dağılım grafiği, farklı hesaplamalardaki değerleri noktalar koleksiyonu olarak tek bir boyut olarak sunar. Çoğu grafikte, boyutunuzu eksenlerden birinde bulursunuz, ancak dağılım grafiği için boyut grafikteki noktalarla gösterilir ve hesaplamalar iki eksenden birinde bulunur. İsteğe bağlı bir üçüncü hesaplama kullanıldığında, değeri kabarcık boyutunda gösterilir. Büyük veri kümelerini analiz ediyor ve sıkıştırılmış verileri görüntülüyorsanız, veri noktalarının yoğunluğu renkle gösterilir.

B.	Bar
      Çubuk grafiği olarak da adlandırılan sütun grafiği, daha uzun sütunların daha büyük sayıları gösterdiği, farklı değerleri karşılaştıran bir grafik türüdür. Sütun grafiği, ayrıca bar grafiği olarak da bilinmektedir. Yatay veya dikey sütun grafikleri oluşturabilirsiniz. Farklı şeylerin boyut veya değer açısından nasıl karşılaştırıldığını göstermek istediğinizde bir sütun grafiği kullanın.

C.	Stem
     Sap-yaprak grafiği olarak da adlandırılan bir gövde-yaprak diyagramı, bireysel veri noktalarını korurken verileri hızlı bir şekilde özetleyen bir diyagram. Böyle bir şemada, "kök", son basamağı çıkardıktan sonra benzersiz veri öğelerinin bir sütunudur.
Benzer şekilde, bir kök grafiği nasıl okursunuz? 'Kök' üzerinde sol ilk basamağı görüntüler veya rakamlar. 'Yaprak' sağdadır ve son rakamı gösterir. Örneğin, 543 ve 548 bir gövde ve yaprak üzerinde birlikte.

Bu seçnekleri kullanıcı istediği gibi doldurduktan sonra algoritmanın ve grafiğin oluşma hızını ayarlıyabilicektir. Bunun yanında grafikte bulunabilicek değer sayısını da belirleyebilmektedir. Grafiklendirmek için seçili değerler uyan grafik modelini “Oluştur” tuşu ile oluştura bilir, “Başlat” tuşu ile hesaplamayı başlatabilir, “Duraklat” tuşu ile hesaplamayı olduğu devrede durdurabilir son olarak “Durdur” tuşu ile işlemi tamamen durdurmuş olur.



HAZIRLIK
•	Uygulamayı çalıştırmak için Python yüklü olmalıdır
•	Python uygulaması içinde “matplotlib” ve “tkinter ” kütüphanelerini indirmelisiniz
•	Github üzerinden Zip dosyasını indirmelisiniz
•	Zip dosyasını açtıkran sonra main.py dosyasını IDE nizde açtıktan sonra çalıştırmalısınız
SIRALAMA ALGORİTMALARI
Kullandığımız algoritmalar:
•	Seçme Sıralaması (Selection Sort)
•	Kabarcık Sıralaması (Bubble Sort)
•	Ekleme Sıralaması (Insertion Sort)
•	Birleştirme Sıralaması (Merge Sort)
•	Hızlı Sıralama (Quick Sort)

I.	Seçme Sıralaması (Selection Sort)
Selection sort manipulates elements in the array "in-place". Due to the time complexity, efficiencies arise when working on large lists.

It has similarities to the insertion sort algorithm presented below. Therefore, if comparing both, selection sort generally performs suboptimally versus insertion sort.
 
II.	Kabarcık Sıralaması (Bubble Sort)
Bubble sort compares adjacent elements and swaps them if they are in the wrong order. The pass of the list repeats to obtain the final ordered values.

Items are seen to bubble to the top of the array, thus giving the algorithm its name. Alternatively, they may sink, which is the other name for this algorithm, sinking sort.

 
III.	Ekleme Sıralaması (Insertion Sort)
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. Wikipedia
 
IV.	Birleştirme Sıralaması (Merge Sort)
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, meaning that the order of equal elements is the same in the input and output. Merge sort is a divide and conquer algorithm.
 
V.	Hızlı Sıralama (Quick Sort)
Quicksort was developed by British computer scientist Tony Hoare in 1959. It is still a commonly used algorithm for sorting. It has potential to be multiple times faster than its main competitors, merge sort and heapsort.
 




