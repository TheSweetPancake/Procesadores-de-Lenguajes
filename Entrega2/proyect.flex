%%
%class analizador
%standalone
%unicode

%init{
    yyline= 1;
    yycolum = 1
}

/* ======== Elementos básicos ======== */

LET              = [A-Za-z]
DIG              = [1-9]
NUM              = 0|{DIG}[0-9]*

PALABRA          = {LET}+

CARACTER_ESPECIAL = [!\"#\$%&'()\*\+,\.\/:;<=>\?@\[\\\]\^_`\{\|\}~\-]

TXT              = ({PALABRA}|{CARACTER_ESPECIAL})( ({PALABRA}|{CARACTER_ESPECIAL}))*

CARACTER_RUTA    = [\\/.: \\-\\\\]
RUTA             = {LET}({LET}|{NUM}|{CARACTER_RUTA})*

EN_CURSO         = En_curso
BOOL             = (Si|No)
NATIVO           = nativo
NIVELVAL         = ([ABC][12 ])
NVHAB_VAL        = (bajo|medio|alto)

BLOCK_COMMENT    = "/\\[\\s\\S]?\\*/"


/* ======== Palabras reservadas ======== */
CV               = cv
DP               = datospersonales
NOMYAPE          = nomyape
FOTO             = foto
FECHA            = fecha
BIO              = bio
CONTACTO         = contacto
EMAIL            = email
TELEFONO         = telefono
REDES            = redes
LINKEDIN         = linkedin
GITHUB           = github
WEB              = web

FORMACION        = formacion
OFICIAL          = oficial
TITULO           = titulo
EXPEDIDOR        = expedidor
DESCRIPCION      = descripcion
LOGROS           = logros
COMPLEMENTARIA   = complementaria
CERTIFICADO      = certificado
HORAS            = horas

IDIOMAS          = idiomas
IDIOMA           = idioma
NIVEL            = nivel

EXPERIENCIA      = experiencia
LABORAL          = laboral
PUESTO           = puesto
RESPONSABILIDADES= responsabilidades
VOLUNTARIADO     = voluntariado
ORGANIZACION     = organizacion

HABILIDADES      = habilidades
SOFT             = soft
HARD             = hard
NVHAB            = nvhab
CATEGORIA        = categoria

PORTAFOLIO       = portafolio
PROYECTO         = proyecto
NOMBRE           = nombre
GRUPO            = grupo
COMPANIERO_N     = compa\u00f1ero
COMPANIERO_TIL   = compa~nero
TECNOLOGIAS      = tecnologias
MERITOS          = meritos

/* ======== Símbolos ======== */
CORCHABR         = "\\{"
CORCHCIE         = "\\}"
PARENABR         = "\\("
PARENCIE         = "\\)"
PUNTOCOMA        = ";"
COMA             = ","

%%

/* ======== Ignorar espacios y comentarios ======== */
[ \\t\\r\\n]+                       { /* ignorar */ }
{BLOCK_COMMENT}                    { /* ignorar */ }

/* ======== Palabras clave (imprimir) ======== */
{CV}                { System.out.println("CV ==> " + yytext(), yyline, yycolum); }
{DP}                { System.out.println("DP ==> " + yytext(), yyline, yycolum); }
{NOMYAPE}           { System.out.println("NOMYAPE ==> " + yytext(), yyline, yycolum); }
{FOTO}              { System.out.println("FOTO ==> " + yytext(), yyline, yycolum); }
{FECHA}             { System.out.println("FECHA ==> " + yytext(), yyline, yycolum); }
{BIO}               { System.out.println("BIO ==> " + yytext(), yyline, yycolum); }
{CONTACTO}          { System.out.println("CONTACTO ==> " + yytext(), yyline, yycolum); }
{EMAIL}             { System.out.println("EMAIL ==> " + yytext(), yyline, yycolum); }
{TELEFONO}          { System.out.println("TELEFONO ==> " + yytext() yyline, yycolum); }
{REDES}             { System.out.println("REDES ==> " + yytext(), yyline, yycolum); }
{LINKEDIN}          { System.out.println("LINKEDIN ==> " + yytext(), yyline, yycolum); }
{GITHUB}            { System.out.println("GITHUB ==> " + yytext(), yyline, yycolum); }
{WEB}               { System.out.println("WEB ==> " + yytext(), yyline, yycolum); }

{FORMACION}         { System.out.println("FORMACION ==> " + yytext(), yyline, yycolum); }
{OFICIAL}           { System.out.println("OFICIAL ==> " + yytext(), yyline, yycolum); }
{TITULO}            { System.out.println("TITULO ==> " + yytext(), yyline, yycolum); }
{EXPEDIDOR}         { System.out.println("EXPEDIDOR ==> " + yytext(), yyline, yycolum); }
{DESCRIPCION}       { System.out.println("DESCRIPCION ==> " + yytext(), yyline, yycolum); }
{LOGROS}            { System.out.println("LOGROS ==> " + yytext(), yyline, yycolum); }
{COMPLEMENTARIA}    { System.out.println("COMPLEMENTARIA ==> " + yytext(), yyline, yycolum); }
{CERTIFICADO}       { System.out.println("CERTIFICADO ==> " + yytext(), yyline, yycolum); }
{HORAS}             { System.out.println("HORAS ==> " + yytext(), yyline, yycolum); }

{IDIOMAS}           { System.out.println("IDIOMAS ==> " + yytext(), yyline, yycolum); }
{IDIOMA}            { System.out.println("IDIOMA ==> " + yytext(), yyline, yycolum); }

/* Las mas faciles no hay que definiarlas, simplemente se crean aqui abajo, y la mas ocmplejas las combinamos y definimos abajo */
