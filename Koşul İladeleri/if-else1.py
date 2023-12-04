'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''
vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

result = (ortalama>=50) and (final>=50)
result = (ortalama >=50) or (final>=70)



if (ortalama>=50):
    if (final>=50):  
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
else:
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')



if (ortalama >=50):
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
else:
    if (final>=70):
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')