---
layout: post
title: "Koşullu ifadeler"
description: "Koşullu ifadelerin kullanımı"
tags: [code, example]
---

### Koşul Operatörleri
* `==`      ->  eşit mi
* `!=`      ->  eşit değil mi
* `< `      ->  küçük mü
* `> `      ->  büyük mü
* `<=`      ->  küçük eşit mi
* `>=`      ->  büyük eşit mi
* `in`      ->  içinde var mı
* `not in`  ->  içinde yok mu
* `is`      ->  eşit mi

## if - elif
`if` koşullu bir ifadeyi belirtirken kullanılır. Ortalama hesaplama örneğini önceki derslerimizde yapmıştık. Bu örnek üzerinde dersten geçme ve kalma koşullarını belirten bir örnek yapalım. Mesela vize ve final ortalamamızı hesaplayıp bu ortalama 40 değerinden küçükse ekrana `geçemediniz`, değilse `geçtiniz` yazdıralım.

{% highlight python %}

vizeStr = input("Vize notunuzu girin: ")
finalStr = input("Final notunuzu girin: ")

vizeInt = int(vizeStr)
finalInt = int(finalStr)

ortalama = (vizeInt + finalInt) / 2

if ortalama < 40:
    print("geçemediniz")
else:
    print("geçtiniz")

{% endhighlight %}


burada `ortalama < 40` gibi bir ifade gördük. Bunun anlamı ortalama 40 değerinden küçük mü sorusunu soruyor ve cevap olarak `True` değeri verirse `if` bloğu diğer durumlarda `else` bloğu çalışıyor.


## if - elif - else
`if` koşulundan başka bir koşul daha belirtilmek istenirse `elif` bloğu kullanılır. Örneğin vize - final ortalaması 40 değeri ve üstünde olanlar ya da final notu 60 ve üzerinde olanlar sınavı geçeçek diğer durumlarda geçemeyecek koşulunu aşağıdaki gibi oluşturabiliriz.

{% highlight python %}

vizeStr = input("Vize notunuzu girin: ")
finalStr = input("Final notunuzu girin: ")

vizeInt = int(vizeStr)
finalInt = int(finalStr)

ortalama = (vizeInt + finalInt) / 2

if ortalama >= 40:
    print("Ortalama ile geçtiniz")
elif final >= 60:
    print("Final notu ile geçtiniz")
else:
    print("geçemediniz")

{% endhighlight %}


burada ise öncelikle `if` koşuluna bakar eğer `if` koşulu `True` değeri alırsa sadece `if` bloğu çalışır, eğer `if` koşulu `False` değeri alırsa `elif` koşuluna bakılır. `elif` koşulu `True` değeri alırsa `elif` bloğu çalışır, eğer `elif` koşulu da `False` değeri alırsa `else` bloğu çalışır.

Birden fazla `elif` koşulu tanımlanabilir ancak `elif` koşulu tanımlanabilmesi için önce `if` koşulu tanımlanmalıdır.

## in
`in` ifadesi ile `list`, `tuple` ve `set` içerisindeki elemanların verilen değeri içerip içermediğine bakılır. Eğer verilen değeri içeriyorsa `True`, içermiyorsa `False` değerini verir.

{% highlight python %}

sehirler = ['bolu', 'yalova', 'istanbul', 'bursa']

if 'ankara' in sehirler:
    print('ankara listede yok')
else:
    print('ankara listede yok')

{% endhighlight %}

## not
`not` ifadesi `bool` değerin tersini alır yani `not True` ifadesi `False` sonucunu, `not False` ifadesi ise `True` sonucunu verir.

{% highlight python %}

sehirler = ['bolu', 'yalova', 'istanbul', 'bursa']

if 'bolu' not in sehirler:
    print('bolu listede yok')
elseif 'yalova' not in sehirler:
    print('yalova listede yok')
elseif 'istanbul' not in sehirler:
    print('istanbul listede yok')
elseif 'bursa' not in sehirler:
    print('bursa listede yok')
else:
    print('listede yok, yok')

{% endhighlight %}

## is
`is` ifadesi `==` yani eşit mi anlamına gelir.

{% highlight python %}

sehirler = ['bolu', 'yalova', 'istanbul', 'bursa']

if (sehirler[2] is 'istanbul'):
    print("ikinci indisteki eleman istanbuldur")
else:
    print("ikinci indisteki eleman istanbul değildir.")

{% endhighlight %}


## and - or
`and` ve `or` iki koşulu bir arada kullanmamızı sağlar. Örneğin final notu `ya da` ortalama 40 değerinden küçükse bu aşağıdaki gibi bir `if` bloğu ile birleştirilebilir.

{% highlight python %}

vizeStr = input("Vize notunuzu girin: ")
finalStr = input("Final notunuzu girin: ")

vizeInt = int(vizeStr)
finalInt = int(finalStr)

ortalama = (vizeInt + finalInt) / 2

if ortalama < 40 or vizeInt < 40:
    print("geçemediniz")
else:
    print("geçtiniz")

{% endhighlight %}

eğer bu ifadeyi final notu `ve` ortalama 40 değeri ve üzerindeyse olarak kurmak istersek ise aşağıdaki gibi bir `if` bloğunda birleştirilebilir.

{% highlight python %}

vizeStr = input("Vize notunuzu girin: ")
finalStr = input("Final notunuzu girin: ")

vizeInt = int(vizeStr)
finalInt = int(finalStr)

ortalama = (vizeInt + finalInt) / 2

if ortalama >= 40 and vizeInt >= 40:
    print("geçemediniz")
else:
    print("geçtiniz")

{% endhighlight %}
