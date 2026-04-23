import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = '''<div class="absolute inset-0 z-0">
<img fetchpriority="high" alt="Corretor de Seguros" class="w-full h-full object-cover object-[75%_center] md:object-center" src="1.png"/>
</div>
<div class="relative z-10 max-w-xl flex flex-col gap-6 items-start text-left">
<h1 class="text-white text-4xl sm:text-5xl lg:text-6xl font-black leading-tight tracking-tight drop-shadow-[0_2px_8px_rgba(0,0,0,0.5)]">
                        O seu seguro <span class="text-primary-light">realmente</span> funciona<span class="hidden sm:inline"> na hora H</span>?
                    </h1>
<p class="sm:hidden text-gray-100 text-base font-normal max-w-[85%] leading-relaxed drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)]">
                        Descubra as lacunas da sua apólice. Montamos a cobertura ideal para você pagar só pelo que precisa.
                    </p>
<p class="hidden sm:block text-gray-100 text-lg sm:text-xl font-normal max-w-xl leading-relaxed drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)]">
                        Descubra as lacunas da sua apólice antes do sinistro. Gustavo Mariano analisa seu perfil e monta a cobertura ideal nas melhores seguradoras — para você pagar só pelo que precisa.
                    </p>'''

pattern = re.compile(r'<div class="absolute inset-0 z-0">\s*<img fetchpriority="high" alt="Corretor de Seguros" class="w-full h-full object-cover" src="1\.png"/>\s*</div>\s*<div class="relative z-10 max-w-xl flex flex-col gap-6 items-start text-left">\s*<h1 class="text-white text-4xl sm:text-5xl lg:text-6xl font-black leading-tight tracking-tight drop-shadow-\[0_2px_8px_rgba\(0,0,0,0\.5\)\]\">\s*O seu seguro <span class="text-primary-light">realmente</span> funciona na hora H\?\s*</h1>\s*<p class="text-gray-100 text-lg sm:text-xl font-normal max-w-xl leading-relaxed drop-shadow-\[0_1px_4px_rgba\(0,0,0,0\.5\)\]\">\s*Descubra as lacunas da sua apólice antes do sinistro\. Gustavo Mariano analisa seu perfil e monta a cobertura ideal nas melhores seguradoras — para você pagar só pelo que precisa\.\s*</p>')

if pattern.search(content):
    content = pattern.sub(new_content, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESS WITH REGEX')
else:
    print('FAILED EVEN WITH REGEX')
