---
layout: post
title: "PyQt5 Kurulumu"
description: "PyQt5 Kurulumu"
tags: [installation, example]
---

# Windows İçin PyQt5 Kurulumu
PyQt5 windows için kurulumunu hızlıca yapabilmemiz için `pyqt.zip` dosyasını indirelim ve `zip` dosyasından çıkartalım. Çıkarttığımızda `pyqt` isimli bir klasör göreceğiz, bu klasörü açalım.

<a style="text-align:center;color:red;text-decoration: none;font-size: 32pt;" href="https://drive.google.com/open?id=1zAS8NDsX0YPRTclv_T8gcYNISsM1sS6C"
target="_blank">pyqt.zip <small style="color:blue;">indir</small></a>

**Kurulumları yaparken:**
* `Python` kurarken `Add PATH` seçeneğini işaretli olmasına dikkat edelim.
* `VisualStudioCode` kurarken `tüm seçeneklerin dolu` olmasına dikkat edelim.

Daha sonra next next şeklinde kurulabiliriz.
Aşağıdaki kurulum dosyalarını _(pyqt klasörünün içinde)_ `sırasıyla` çalıştıralım.

### Kurulum Dosyaları
* `python-3.7.0-amd64.exe`
* `VSCodeUserSetup-x64-1.27.2.exe`
* `PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x32-2.exe`
* `install.bat`


Kurulumu burada bitirmiş olduk. Artık `VisualStudioCode` programını açarak kullanabiliriz.

## ÖNEMLİ
Eğer `VisualStudioCode` içerisinde sağ tıkladığımız menüleri bulamıyorsak, `VisualStudioCode` içerisindeki `extension` kısmından `Python` ve `Pyqt Integration` eklentilerini aktif duruma getirmemiz gerekebilir ya da yine bu menüden bu eklentileri kurabiliriz.

{% include image.html path="vscode-extension-installation.png" path-detail="vscode-extension-installation.png" alt="Visual Studio Code Extension Kurulumu" %}
