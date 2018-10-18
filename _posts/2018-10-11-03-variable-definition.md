---
layout: post
title: "Değişken tanımlama"
description: "Değişken tanımlama nasıl yapılır"
tags: [code, example]
---

Değişkenler uygulamamızı dinamikleştirmemize sağlayan bir yapıdır. Aşağıdaki gibi değişken kullanılmadan yazılmış bir uygulama örneğini incelersek,

{% highlight python %}

print("Bolu Otogara Hoşgeldiniz...")
print("Biletin verildigi otogar: Bolu")
print("Bolu otogarı kullandıginiz icin tesekkur ederiz!")

{% endhighlight %}

bu uygulamanın Bolu ilinde çalışan bir bilet uygulaması olduğunu anlamaktayız. Eğer bu uygulamayı İstanbul ilinde kullanmak istersek yapmamız gereken Bolu yazan yerleri İstanbul olarak güncellemektir. Burada 3 satır da Bolu geçtiğinden bu uygulamada Bolu yazan kısımların nerede olduğunu biliyoruz ve az olduğundan hızlıca değiştirebiliriz. Ancak bu uygulamamızın çok daha büyük bir uygulama olduğunu düşünürsek, Bolu yazan kısımların nerede olduğunu ve kaç tane satırda değişiklik yapacağımızı bilemeyiz. Bu yüzden Bolu ifadesini değişken olarak tanımlayıp bu şekilde kullanmalıyız. Yukarıdaki bilet uygulamasının değişken tanımlanarak uygulanması aşağıdaki gibidir.

{% highlight python %}

sehir = "Bolu"

print(sehir, "Otogara Hoşgeldiniz...")
print("Biletin verildigi otogar:", sehir)
print(sehir, "otogarı kullandıginiz icin tesekkur ederiz!")

{% endhighlight %}

Burada print komutu artık `sehir` yazan kısımlara Bolu yazacaktır. Çünkü `sehir` tırnak ile tanımlanmadığı için bir `string` ya da bir sayı olmadığından `integer` bir değer de değildir. Ozaman python dili bu ifadeyi değişken olarak okumaya çalışır. Eğer yukarıda `sehir = "Bolu"` gibi bir ifade olmasaydı, `sehir` gördüğü kısımlara ne yazacağını bilemeyecek ve hata verecekti. Bu yüzden bir değişkeni kullanmadan önce bu değişken yerine ne yazacağımızı bildirmemiz gerekir. Yani `DEGISKENADI = DEGER` olarak bir değişken tanımlamamız gerekir.