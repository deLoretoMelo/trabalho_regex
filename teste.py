import funcoes

# Cadeias de teste para o estresse das funções
nomes_teste = ["Eduardo Albuquerque", "Jo@o Pedr0 V@sconcelo$", "Ad E T", "Marcelo melo", "V1rg1l1o N3t0", "Ladielma Carina Santos Teixeira",  "caroline", "Jonas1 Tomilho", "Calandrinix #nias", "alina Sardinha", "sANDRA cASSANDRA", "Jonas Dantas Teixeira", "Joao Lucas", "CarlosAugusto", "Mauricio Cardoso Silveira"]

emails_teste = ["lianC@gmail.com.br", "AnyIla@com.br", "123.com.br","@gmail.com.br", "anivcina@hotmail.com.br", "@oter.com.br", "##@ctrl.com.br", "andre@ufpa.br", "ana@hotmail.br", "cptx@word.com.br", "dani@brs.com", "SZA@GMAIL.COM.BR", "@gmail.com.br", "mandila@ufpa.br","will@gmail.br"]

senhas = ["kvy487", "Q3ut9", "LEtSPK4d", "su1672wm", "nNOyDdL8", "t1.uqXcfc", "np9x7NoB", "DBUaCJ05", "DEGes2t31v", "kXS+8r5u", "KSR43ED4", "kcs9.d'aa", "Ets493Qs", "okgv990c", "JDSJAISS"]

cpfs = ["952.054.440-29", "555.635.190-23", "37681410040", "51.728.580-09", "407.182.170-125", "491.623.160-01", "187.673.420-02", "9l8.479.910-73", "345.728.830-06", "aLS.As@.^sf.dd", "213.437.864.55", "012.781.996", "934-604-049-72", "018.658.852-66","299.556.043-92"]

telefones = ["(61) 92065-1842", "83000938073770", "(83) 932640687", "5593752-3542", "63 935140454", "69927105345", "(85)82722-0241", "(539) 92714-3575", "62 92896-0044", "(73)92663-9162", "(85) 92931-37118", "(28)936067596", "32 9434-900", "(51) 99423-7768", "91 98349-0032"]

datas = ["2017-06-26 19:36:14", "20/07/2012 14:05:51", "04/09/1970 09:11:01", "02/10/2022/ 01:28:08", "11/16/2016 8:9:5", "03.26.1974 18:38:43", "14:57:14 05/06/1997", "07/15/1971-05/03/52", "07/25/198318:12:39", "06/22/ 1979 03:42:21", "12/13/1980 03:25:30", "03/05/1991 17:04:02", "94/15/1275 72:43:34", "21/02/12 12:33:21", "24/12/3124 51:32:12"]

numeros = ["18", "-83", "-92,69", "+8.9", "-32.0", ".1", "a", "+68", "12.-4", "+", "-156.66516", "0", "-23.33", "+@.#", "132."]

arranjos_a = ["HMhhhm", "MMmhm", "Mhm", "MHh", "HHmhmhmh", "MHMhh", "MHmhmhmmhh", "MM", "MH", "HMhhmmh", "MMhhh", "HHmmmmh","MHmmhhhhhh","MHMH","Hmmh"]

arranjos_b = ["MHmmmh", "MHhhmmh", "HMmhmhmhh", "Mhhm", "HMmhmmmmhmhm", "MHm", "MMmmm", "MMhhhmmmh", "HMmmh", "HMmmhhm", "mmhhhhm", "HHmmhhhhh", "MHmhmhmhhmhmhmhmhhmmhhmm", "HMmhhm", "HMMHmmmh"]

arranjos_c = ["HMmhhmh", "HMhhmhhm", "MHmhhhmmh", "HHmmmh", "HHMhhmmhm", "HMmh", "MMmhmhmmh", "MHhmmhh", "MHmhmmh", "HHHmmhh", "HMmmh", "hmm", "Mmmh", "HMhmh", "MHmmmhhh"]

arranjos_d = ["HHmhhhmmhmh", "MMhhm", "MHhmhhmhmmh", "HHMhmmhh", "MMmhhhmmhmhm", "HHmh", "HHmmhhmhh", "MMhmhhmmmhhm", "MHhmhhmmhmhmmhm", "MMhmmhhmmmmmmmhhmmh", "HHmmmmmmmmmm", "HHHmhmmmmmhm", "HH", "MMhmhmhmhm", "HMhhhmmmhh"]

arranjos_e = ["HHmhhmh", "MMmhmhm", "HMhmhmhhh", "MMhmhmhmh", "MMhhmhhmhh", "MMhmhmhmhmhmhmhmhmh", "HHmh", "MH", "MHhmhmhm", "MMhmhmh", "HHmhmhh", "MMhmhmhmhm", "HHHHmhmh", "MM", "MHmh"]

arranjos_f = ["HHmhmhmmhhmhm", "MMmmmmmmm", "HHmhhmhhmmhhmmmhhmmhh", "HHhmmmmmmmmmmmh", "MMhmhhmh", "HMhmmh", "HHhmhmhhmmh", "MMh", "MMmmhmmmhmmmmh", "MMhm", "HHhhhhhhhh", "MMhmhhh", "HHmhmhm", "HH", "HMmmhmhmhmm"]

arranjos_g = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


#chamada das funções para a execução dos testes
funcoes.teste_estresse(arranjos_d, funcoes.d)
