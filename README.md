# Huruf

Bu proje, Kuran'da Huruf-u Mukattaa adı verilen harflerin analizi için oluşturulmuştur. 

Bu 12 harf, Kuran'daki 29 surenin başında bulunur. Listesi şöyledir: "ayn", "elif", "ha", "kaf", "lam", "mim", "nun", "ra", "ta", "sad", "sin", "ya"

Projedeki kodlamalar Python dilindedir.

Proje kapsamında yapılan incelemelerde; harfler ile sure içerikler arasında bir korelasyon bulunmamıştır.

Bu GitHub projesi, farklı fikirleri olan kişilerin zaman kaybetmeden araştırmaya devam edebilmesi için
halka açılmıştır.

## Yapılan çalışma

### Hazırlık

Kuran metni Türkçe ve İngilizce olarak indirilmiş, XML ve CSV formatlarına çevrilmiştir. Bu dosyalara
**data** klasörü altından erişilebilir. Bu içeriğe kolay erişim için, **model** klasörü altında bulunabilecek 
yardımcı yordamlar oluşturulmuştur.

### Ayetleri atlayarak okumak 

Huruf-u Mukattaa harflerinin Arap alfabesindeki sıralarının sayısal bağlamda bir anlama gelebileceği düşüncesiyle
inceleme yapıldı. İlgili suredeki ayetleri; harflerin alfabedeki sırasına göre atlaya atlaya okumayı denedim. 
Anlamlı bir sonuç çıkmadı. 

### Checksum

Alfabedeki sıralarının; ilgili surenin içeriğini valide edip koruyacak bir Checksum olabileceğini düşündüm.
Ancak; çeşitli yöntemlerle surenin kelime, harf, ünlü harf, vs sayılarını incelememe rağmen, 
başlarındaki huruf-u mukattaa harfleri ile aralarında bir korelasyon tespit edemedim.

Bu çalışmaya, http://www.qurananalysis.com/analysis/basic-statistics.php?lang=EN adresindeki istatistikler
epey yardımcı oldu.

### Surede geçme sayısı

Huruf-u mukattaa harflerinin ilgili surede kaç kez geçtiğini tespit ederek bir korelasyon
aradım ancak çıkmadı. Mesela; elif 1. harf, lam 23. harf, mim 24. harftir. Bu harfler; 2, 3, 29, 30, 31, 32.
surelerin başlarında geçmektedir. Her bir surede her bir harfin kaç kez geçtiğine bakarsak;

- 2: 286 12316 52639 
- 3: 200 7080 30276
- 29: 69 1969 8353
- 30: 60 1636 7003
- 31: 34 1038 4415
- 32: 30 745 3153   

Burada bir ilişki tespit edemedim. Merak edenler, harflerle ilgili istatistiklere 
http://www.intellaren.com/articles/en/qss adresinden erişebilir. 

### Sure içerikleri

Huruf-u mukattaa harflerinin; ilgili surelerin içerdiği konularla ilgili bazı işaretler barındırabileceği
düşüncesiyle bir inceleme gerçekleştirdim. Bu incelemede; Türkçe dilindeki ekler kelimeleri değiştirdiği
için İngilizce metni baz aldım.

**tdc.ipynb** dosyasında görülebilecek bir Machine Learning uygulaması gerçekleştirdim; teknik adıyla
Supervised Text Classification yaptım. Naive Bayes, Linear SVC, Logistic Regression algoritmalarıyla
incelememe rağmen; %100'e yaklaşan bir korelasyon çıkmadı. Burada yaptığım araştırma, 
https://towardsdatascience.com/multi-label-text-classification-with-scikit-learn-30714b7819c5 adresindeki
örneğe dayanmaktadır.

Akabinde; kelime bulutu mantığıyla ayetlerde sık geçen kelimeleri öne çıkararak bir karşılaştırma yaptım;
detaylar **ml/huruf_word_cound.py** dosyasında görülebilir. Ancak; burada da belirgin bir dağılım
tespit edemedim.

## Yapılmayanlar

Aşağıdaki adımlar aklımdan geçmesine rağmen uygulamadım:

- Huruf-u mukattaa harflerinden (alfabedeki sıra hariç) başka sayısal değerler çıkartılarak, üstteki 
çalışmalar tekrarlanabilir. Örneğin bunların benzediği sayılar vardır belki?

- Bu hurufların çok boyutlu bir düzlemin koordinatları olabileceği ve sureleri bu düzleme yerleştirerek
yukarıdan aşağı / sağdan sola okumanın bazı örtüleri kaldırabileceği aklımdan geçti. Ancak; harfsiz,
tek harfli veya 5-6 harfli sureler olduğundan; bu fikri uygulayabileceğim bir bağlam bulamadım. 

- Toplam 12 huruf-u mukattaa olması ile 12 ay olması arasında bir bağlantı olup olamayacağı aklımdan
geçti, ancak bu fikri materyalize edecek bir bağlam bulamadım.

## Proje yapısı

**data** dizini içerisinde, Kuran-ı Kerim metni
bulunmaktadır.

- **kuran.csv**: CSV formatında Türkçe Kuran metnidir (Şaban Piriş)
- **kuran.xml**: XML formatında Türkçe Kuran metnidir (Şaban Piriş)
- **kuran-en.csv**: CSV formatında İngilizce Kuran metnidir
- **kuran-en.xml**: XML formatında İngilizce Kuran metnidir
- **ml_all.csv**: Machine Learning algoritmalarına uygun olarak tasarlanmış; Huruf-U Mukattaa içeren ayetleri ve Label'ları içeren CSV dosyasıdır. 

**ml** dizini içerisinde, Machine Learning araştırmalarına ait destekleyici dosyalar bulunmaktadır.

- **csv_generator.py**: ml_all.csv dosyasını oluşturmak için kullanılan koddur. Dosya oluştuğu için, artık bu koda gerek kalmamıştır. Ancak ileride tekrar gerekirse kullanılabilir.
- **huruf_word_count.py**: Ayetlerde sık geçen kelimeleri Word Cloud şeklinde HTML formatında çıkarır. 

**model** dizini içerisinde, Kuran içeriğine erişimi kolaylaştıracak sınıflar bulunmaktadır.

- **arabic_alphabet.py**: Arapça harfleri latin alfabesiyle barındırır.
- **ayet.py**: Ayet nesnesi. Ayet içerikleriyle ilgili yardımcı yordamlar içerir.
- **huruf.py**: Huruf-u Mukattaa nesnesi. Bu özel harflerle ilgili yardımcı yordamlar içerir.
- **kuran.py**: Kuran-ı Kerim nesnesi. Kitap içeriğine erişimle ilgili yardımcı yordamlar içerir.
- **sure.py**: Sure nesnesi. Sure erişimiyle ilgili yardımcı yordamkar içerir.

Kök dizinde ise, ana nesneler bulunmaktadır.

- **main.py**: Programla ilgili ana işlevler
- **tdc.ipynb**: Machine Learning denemeleri için kullanılmış Jupyter Notebook

## Limitasyonlar

Arapça bilmediğim için, araştırmalar sırasında gözden kaçan pek çok detay olmuş olabilir. Arap dilinin başka dillere 
yansıtılamayacak incelikleri arasında sayısal bir araştırma yaparak, Huruf-u Mukattaa'nın anlamları belki de
çıkarılabilir. 