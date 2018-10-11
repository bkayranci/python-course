---
layout: post
title: "Veri tipleri"
description: "Python dilinde veri tipleri"
tags: [code, example]
---

Anlatacağımız veri tipleri:
* int
* float
* str
* list
* tuple
* dict

### int
'int' tipini tam sayılar olarak ifade edebiliriz. Tam sayılı ifadeler ile gündelik yaşamda nasıl dört işlem yapılabiliyorsa `int` değerler ile de dört işlem yapılabilir. Uygulamamızı dinamik bir hale getirmek amacıyla bu değerleri bir değişkene tanımlayıp bu değişkenler arasında dört işlem yaptırılabilir. Örneğin vize ve final notlarımızın ortalamasını hesaplatmak için bir uygulamayı aşağıdaki gibi

#### değişken tanımlamadan

{% highlight html %}

print("Ortalama:", (70 + 80) / 2)

{% endhighlight %}

#### değişken tanımlayarak

{% highlight html %}

vize = 70
final = 80

ortalama = (vize + final) / 2
print("Ortalama:", ortalama)

{% endhighlight %}

şeklinde yapabiliriz. Değişken tanımlamak tanımladığımız ifadeyi daha sonra da tekrar tekrar kullanmamızı sağlar.

### float
`float` tipini ondalık sayılar olarak tanımlayabilir ve bu sayılar ile de dört işlem yapabiliriz. Örneğin vize sınavından 70.75 alabiliriz. Bu durumda uygulamamızı aşağıdaki gibi günceller `vize` değişkeninin ondalık kısmını nokta ile ayırırız.

{% highlight html %}

vize = 70.75
final = 80

ortalama = (vize + final) / 2
print("Ortalama:", ortalama)

{% endhighlight %}

Bölme işlemi bize `float` bir sonuç verir ve eğer bölümden tam sayı elde etmişsek sayının sonuna `.0` ekleyerek gösterir. Eğer hassas bir bölme işlemi yapmak istemiyorsak, `/` yerine `//` operatörünü kullanarak ondalık kısmı silinmiş bir integer sonuç elde ederiz.

### str
`str` tipini yazı olarak tanımlayabiliriz. `"` ya da `'` arasına yazılmış her ifadeyi bilgisayarımız yazı tipinde algılar. Örnek olarak bir yazıyı ekrana yazdırma işlemini aşağıdaki gibi yapabiliriz.

{% highlight html %}

print("Türkiye")
print('Türkiye')

ulke = "Türkiye"
print(ulke)

sehir = 'Bolu'
print(sehir)

{% endhighlight %}

### list
`list` tipini liste olarak tanımlarız. Örneğin bir marketin ürünler listesi, alınacaklar listesi, fiyatlar listesi gibi bir çok listeyi `list` tipinde kullanırız. `list` tipinde bir ifade `[` ile `]` arasında tanımlanır. Bir listeyi aşağıdaki gibi  ekranda gösterebiliriz.

{% highlight html %}

print(["bolu", "yalova", "istanbul"])
print([1, 2, 3])

sehirler = ["bolu", "yalova", "istanbul"]
print(sehirler)

harcamalar = [6, 3, 8]
print(harcamalar)

{% endhighlight %}

Liste tanımlamayı çok tane değişken tanımlamak olarakta görebiliriz. Yani yukarıdaki örnekteki `sehirler` listesinin elemanlarından `bolu` yu yani 1. elemanı kullanmak istersek `sehirler[0]` yazarak 1. elemanın indis değeri olan `0` ile bu listenin ilk elemanına ulaşabiliriz. Burada dikkat etmemiz gereken önemli nokta indis değerlerinin sıfırdan başlamasıdır. Örneğin bir listenin 25. elemanına ulaşmak için `herhangibirliste[24]` yazmamız gerekir. `sehirler` listesinin 1.elemanını ekrana yazdırmak istersek bunu aşağıdaki gibi yapabiliriz.

{% highlight html %}

sehirler = ["bolu", "yalova", "istanbul"]
print(sehirler[0])

{% endhighlight %}

Liste içinde sadece `str` ya da `int` ifadeler olmasına gerek yoktur. Her tipten veri bulunabilir ve karışık bir liste tanımlanabilir. Sonradan bu listeye eleman eklenebilir ve bu listeden eleman silinebilir.

#### listeye veri ekleme
`list` tipinde bir değişkene `append` fonksiyonu ile eleman eklenebilir. Örneğin şehirler listemize bursa değerini ekleyelim.

{% highlight html %}

sehirler = ["bolu", "yalova", "istanbul"]
sehirler.append("bursa")

print(sehirler)

{% endhighlight %}

#### listeden veri çıkarma
`list` tipinde bir değişkenden `remove` ve `pop` fonksiyonu ile eleman çıkarılabilir. Remove  ile pop fonksiyonunun farkı ise remove fonksiyonu girdi değeri olarak silmek istediğimiz elemanı isterken pop fonksiyonu sonuncu elemanı siler. Ayrıca remove fonksiyonu geri hiçbir şey döndürmezken pop fonksiyonu sildiği elemanı geri döndürür. Örneğin şehirler listemizden bolu değerini ve sondaki elemanı çıkaralım.

{% highlight html %}

sehirler = ["bolu", "yalova", "istanbul"]
sehirler.remove("bolu")

sehirler.pop()

{% endhighlight %}

### tuple
`tuple` veri tipi `list` veri tipine çok fazla benzemektedir. Ancak listeden bazı farkları ile öne çıkmaktadır. `(` ile `)` arasında tanımlanır. `list` tipinde bir değişkene eleman ekleme ve çıkarma yapılabilirken `tuple` tipinde bir listeye ekleme ve çıkarma işlemleri yapılamaz.


### dict
`dict` veri tipi bize daha okunabilir ve daha kullanışlı bir yapı sağlar. Örneğin bir şehrin nüfus değerini, ilçe sayısı değerini tuttuğumuz bir liste tanımlayalım.

{% highlight html %}

bolu = [250000, 10]

print(bolu)

{% endhighlight %}

Eğer ekrana bolu değişkeninin yani Bolu'nun nüfusunu yazdırmak istersem `bolu[0]` diye bir ifade kullanacağım. Bu durumda uygulamamızı geliştiren bir yazılımcı ekrana ilçe sayısını yazdırmak istediğinde Bolu ilini değişken adından anlayabilecek ama 2.elemanda yani 1. indiste bu değerin tutulduğunu anlayamayacak. Bu durumdan kurtulmak için `dict` veri tipi kullanılır.

{% highlight html %}

bolu = {"nufus": 250000, "ilcesayisi": 10}

print(bolu['ilcesayisi'])

{% endhighlight %}

### Veri tipini öğrenme
`type` fonksiyonu girdi olarak verilen değerin ya da daha önceden tanımlanmış bir değişkenin veri tipini öğrenmemizi sağlar. Örneğin, 

{% highlight html %}

print(type(5))

bolu = {"nufus": 250000, "ilcesayisi": 10}

print(type(bolu))

{% endhighlight %}