# Conectados com Consciência

Campanha de conscientização em segurança digital, com edições mensais pensadas para o dia a dia, no trabalho e em casa. Aqui está o material que produzi: boletins, infográficos, quadrinho, um plano de um mês de campanha e um estudo de caso real.

> **Sobre este repositório:** a campanha foi planejada para uma empresa, mas não chegou a ser lançada. Em vez de deixar o material parado, organizei tudo aqui como portfólio e como arquivo, para que qualquer pessoa possa reaproveitar.

## Objetivo

Mostrar segurança digital sem jargão, para quem não é da área. A ideia é que cada pessoa leia em poucos minutos, entenda o risco e saia com uma ação prática. Quem protege a própria conta em casa também protege a empresa.

## Como cada edição é montada

Todas as edições seguem o mesmo formato, o que facilita produzir e manter a campanha:

1. **Tema do mês**, com o contexto do risco
2. **Dica rápida**, com ações práticas
3. **Você sabia?**, com um fato que gera curiosidade
4. **Desafio rápido**, com uma pergunta de múltipla escolha e a resposta explicada
5. **Link útil**, com uma fonte confiável (em geral, as cartilhas do CERT.br)
6. **Frase do mês**, para fixar a ideia

## Edições

| # | Tema | Ler e baixar |
|---|------|----------|
| 1 | Senhas seguras | [Ler online](posts/edicao-01-agosto-senhas.html) · [PDF](edicoes/pdf/edicao-01-agosto-senhas.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-01-agosto-senhas.pdf) |
| 2 | Phishing | [Ler online](posts/edicao-02-setembro-phishing.html) · [PDF](edicoes/pdf/edicao-02-setembro-phishing.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-02-setembro-phishing.pdf) |
| 3 | Privacidade digital | [Ler online](posts/edicao-03-outubro-privacidade.html) · [PDF](edicoes/pdf/edicao-03-outubro-privacidade.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-03-outubro-privacidade.pdf) |
| 4 | Golpes em mensagens (WhatsApp e SMS) | [Ler online](posts/edicao-04-novembro-golpes-mensagens.html) · [PDF](edicoes/pdf/edicao-04-novembro-golpes-mensagens.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-04-novembro-golpes-mensagens.pdf) |
| 5 | Riscos do Wi-Fi aberto | [Ler online](posts/edicao-05-dezembro-wifi-aberto.html) · [PDF](edicoes/pdf/edicao-05-dezembro-wifi-aberto.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-05-dezembro-wifi-aberto.pdf) |
| 6 | Segurança no celular | [Ler online](posts/edicao-06-janeiro-celular.html) |
| 7 | Deepfakes e desinformação | [Ler online](posts/edicao-07-fevereiro-deepfakes-desinformacao.html) |
| 8 | Golpes financeiros online | [Ler online](posts/edicao-08-marco-golpes-financeiros.html) |
| 9 | Redes sociais: pessoal e profissional | [Ler online](posts/edicao-09-abril-redes-sociais.html) |
| 10 | Engenharia social | [Ler online](posts/edicao-10-maio-engenharia-social.html) |
| 11 | Atualizações de sistema | [Ler online](posts/edicao-11-junho-atualizacoes.html) |
| 12 | Vazamento de dados | [Ler online](posts/edicao-12-julho-vazamento-de-dados.html) |
| 13 | Backups | [Ler online](posts/edicao-13-agosto-backups.html) |

**Edições especiais:** [PDF perigoso](posts/especial-pdf-perigoso.html), [como funciona um ataque com PDF malicioso](posts/especial-ataque-com-pdf-passo-a-passo.html) (visão geral, sem instruções operacionais) e [credenciais salvas no navegador](posts/especial-credenciais-salvas.html).

## O que tem em cada pasta

| Pasta | Conteúdo |
|-------|----------|
| [`posts/`](posts/) | Páginas do site: uma por edição, mais as edições especiais |
| [`edicoes/`](edicoes/) | Boletins em PDF simples e colorido (edições 1 a 5) |
| [`infograficos/`](infograficos/) | Infográficos e checklist em HTML, informativos de senhas (versão geral e técnica) e quadrinho |
| [`plano-agosto-senhas/`](plano-agosto-senhas/) | Plano semanal de um mês de campanha, com informativos geral e técnico sobre senhas |
| [`casos/cisco-2022/`](casos/cisco-2022/) | Estudo de caso do incidente da Cisco em 2022: senha vazada e MFA burlado |
| [`ameacas/`](ameacas/) | Mapa dos tipos de ameaças cibernéticas |
| [`referencias/`](referencias/) | Fontes externas usadas (os links, não os arquivos) |

## Como rodar um mês de campanha

O [plano semanal](plano-agosto-senhas/plano-semanal-agosto.pdf) mostra um mês completo sobre senhas:

- **Semana 1:** boletim do mês e um quadrinho leve, para quem não vai ler o texto inteiro
- **Semana 2:** informativo geral explicando como senhas são quebradas
- **Semana 3:** versão técnica para quem é de TI (funções de hash, tipos de ataque)
- **Semana 4:** caso real para fixar o aprendizado (Cisco 2022)

Dá para repetir a mesma estrutura em qualquer um dos outros temas.

## Estudo de caso: Cisco 2022

Uma conta pessoal comprometida, uma senha reaproveitada e um MFA contornado foram o ponto de partida do incidente. A pasta [`casos/cisco-2022/`](casos/cisco-2022/) resume o caso em linguagem acessível. Para o relato técnico completo, use a fonte original da Cisco Talos: <https://blog.talosintelligence.com/recent-cyber-attack/>.

## Site

O repositório tem um site estático (`index.html` e `posts/`) com uma página por edição. Para publicar no GitHub Pages: em **Settings → Pages**, escolha a branch `main` e a pasta `/ (root)`. O endereço fica `https://maisareis.github.io/<nome-do-repositório>/`.

## Avisos

- Este material é educativo e foi escrito em linguagem acessível. Ele simplifica propositalmente alguns conceitos técnicos.
- As estatísticas citadas vêm das fontes indicadas em cada material. Confira a fonte original antes de reutilizar um número.
- Os e-mails de exemplo nos infográficos são fictícios.

## O que eu aprendi

- Um formato fixo por edição reduz muito o esforço de produzir todo mês.
- Duas versões do mesmo tema (geral e técnica) atendem públicos diferentes sem precisar de duas campanhas.
- Um caso real dá peso ao risco: as pessoas lembram da história, não da lista de dicas.
- Se fosse lançar, eu definiria as métricas antes (taxa de abertura, resultado dos desafios, simulação de phishing) para poder medir de verdade.

## Autoria e licença

Criado por **Maisa Reis Araujo** ([@maisareis](https://github.com/maisareis)).

Licença [CC BY-NC-SA 4.0](LICENSE.md): você pode usar, adaptar e compartilhar, desde que dê o crédito, não use para fins comerciais e mantenha a mesma licença.
