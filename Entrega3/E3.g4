grammar CVantlr4;

// ======== Palabras clave ========
CV              : 'cv' ;
ID              : 'id' ;
GVAR            : 'gvar' ;
LVAR            : 'lvar' ;

DP              : 'datospersonales' ;
NOMYAPE         : 'nomyape' ;
FOTO            : 'foto' ;
FECHA           : 'fecha' ;
BIO             : 'bio' ;
CONTACTO        : 'contacto' ;
EMAIL           : 'email' ;
TELEFONO        : 'telefono' ;
REDES           : 'redes' ;
LINKEDIN        : 'linkedin' ;
GITHUB          : 'github' ;
WEB             : 'web' ;

FORMACION       : 'formacion' ;
OFICIAL         : 'oficial' ;
TITULO          : 'titulo' ;
EXPEDIDOR       : 'expedidor' ;
DESCRIPCION     : 'descripcion' ;
LOGROS          : 'logros' ;
COMPLEMENTARIA  : 'complementaria' ;
CERTIFICADO     : 'certificado' ;
HORAS           : 'horas' ;

IDIOMAS         : 'idiomas' ;
IDIOMA          : 'idioma' ;
NIVEL           : 'nivel' ;

EXPERIENCIA     : 'experiencia' ;
LABORAL         : 'laboral' ;
PUESTO          : 'puesto' ;
RESPONSABILIDADES: 'responsabilidades' ;
VOLUNTARIADO    : 'voluntariado' ;
ORGANIZACION    : 'organizacion' ;


HABILIDADES     : 'habilidades' ;
SOFT            : 'soft' ;
HARD            : 'hard' ;
HABILIDAD       : 'habilidad' ;
NVHAB           : 'nvhab' ;
CATEGORIA       : 'categoria' ;

PORTAFOLIO      : 'portafolio' ;
PROYECTO        : 'proyecto' ;
NOMBRE          : 'nombre' ;
GRUPO           : 'grupo' ;
COMPAÑERO       : 'compañero' ;
TECNOLOGIAS     : 'tecnologias' ;
MERITOS         : 'meritos' ;


// ======== Símbolos ========
LL_A            : '{' ;
LL_C            : '}' ;
PA_A            : '(' ;
PA_C            : ')' ;
IG              : '=' ;
PYC             : ';' ;
CO              : ',' ;
CD              : '"' ;

// ======== Comentarios estilo C ========
ERR_COMMENT_CLOSE
    : '*/' { System.err.println("Error léxico: cierre de comentario sin apertura"); skip(); }
    ;

COMMENT
    : '/*' .*? '*/'      { skip(); }                      // Comentario bien cerrado
    | '/*' .*?  EOF      { System.err.println("Error léxico: comentario no cerrado antes del fin de archivo"); skip(); }
    ;

// ======== Macros ========
TFNO            : ([5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]) ;
NUM             : ('0' | [1-9][0-9]*) ;
PAL             : [A-Za-zÁÉÍÓÚáéíóúÑñ]+ ;
IDENT           : CD PAL {PAL|NUM} CD ;
MAIL            : [A-Za-z0-9]+ ('.' [A-Za-z0-9]+)* '@' [A-Za-z0-9]+ ('.' [A-Za-z0-9]+)* ;
RUTA            : [A-Za-z]+ ( [./\-:]+ [A-Za-z]+ )+ ;
FECHA_NUM       : ('0'[1-9] | [12][0-9] | '30' | '31') '/' ('0'[1-9] | '1'[0-2]) '/' ([12][0-9][0-9][0-9]);
BOOL            : 'Si' | 'No' ;
NVI             : ([ABC][12]) | 'nativo' ;
NVH             : 'bajo' | 'medio' | 'alto' ;

// ======== Espacios y saltos de línea ========
WS              : [ \t\r\n]+ -> skip ;

// ======== token CONJPAL (conjunto de palabras) ========
CONJPAL         : '"' (PAL (WS PAL)*)? '"' ;
CONJPALYNUM         : '"' (PAL (WS PAL | WS NUM)*)? '"' ;

// ======== Manejo de errores ========
ERROR : . { System.err.println("Error léxico: carácter no reconocido " + getText()); } ;

// ========== Sintaxis ==========
cvs:            (global_var? (cv)+) ;
        
global_var:     GVAR LL_A variable LL_C ;
local_var:      LVAR LL_A variable LL_C;
variable:       IDENT IG CONJPALYNUM PYC ;

cv:             CV IDENT LL_A local_var datospersonales formacion idiomas? experiencia? habilidades? portafolio? LL_C ;

datospersonales:DP LL_A nomyape foto? fecha bio? contacto LL_C ;
nomyape:        NOMYAPE PA_A CONJPAL+ PA_C ;
foto:           FOTO PA_A RUTA PA_C ;
fecha:          FECHA PA_A FECHA_NUM PA_C ;
bio:            BIO PA_A CONJPALYNUM PA_C ;
contacto:       CONTACTO LL_A email telefono redes LL_C ;
email:          EMAIL PA_A MAIL PA_C ;
telefono:       TELEFONO PA_A (TFNO | NUM) PA_C ;
redes:          REDES (linkedin github? web?
            |   linkedin? github web?
            |   linkedin? github? web);
linkedin:       LINKEDIN PA_A RUTA PA_C ;
github:         GITHUB PA_A RUTA PA_C ;
web:            WEB PA_A RUTA PA_C ;

experiencia:    EXPERIENCIA LL_A (laboral+ voluntariado* | voluntariado+) LL_C;
formacion:      FORMACION LL_A oficial+ complementaria* LL_C ;
oficial:        OFICIAL LL_A titulo expedidor descripcion? logros? fecha LL_C ;
titulo:         TITULO PA_A CONJPAL+ PA_C ;
expedidor:      EXPEDIDOR PA_A CONJPAL+ PA_C ;
descripcion:    DESCRIPCION PA_A CONJPALYNUM PA_C ;
logros:         LOGROS PA_A CONJPALYNUM PA_C ;

idiomas:        IDIOMAS LL_A idioma+ LL_C ;
idioma:         IDIOMA LL_A NOMBRE NIVEL PA_A NVI PA_C expedidor? LL_C  ;

complementaria: COMPLEMENTARIA LL_A titulo certificado? expedidor horas? fecha LL_C;
certificado:    CERTIFICADO PA_A BOOL PA_C;

laboral:        LABORAL LL_A organizacion puesto horas responsabilidades? LL_C;
puesto:         PUESTO PA_A CONJPALYNUM PA_C;
responsabilidades: RESPONSABILIDADES PA_A CONJPALYNUM PA_C;
voluntariado:   VOLUNTARIADO LL_A puesto descripcion horas organizacion LL_C;
organizacion:   ORGANIZACION PA_A CONJPALYNUM PA_C;

habilidades:    HABILIDADES LL_A soft hard* LL_C| HABILIDADES LL_A hard+ LL_C;
soft:           SOFT LL_A habilidad(CO habilildad)* LL_C;
hard:           HARD LL_A categoria+ LL_C;

nvh:            NVHAB PA_A NVH PA_C;
habilidad:      HABILIDAD PA_A CONJPALYNUM PA_C;
categoria:      CATEGORIA PA_A NOMBRE (HABILIDAD NVHAB)+ PA_C;

portafolio:     PORTAFOLIO LL_A (proyecto+ merito* | merito+) LL_C;
proyecto:       PROYECTO LL_A nombre grupo? descripcion categoria tecnologias web? LL_C;

nombre:         NOMBRE PA_A CONJPALYNUM PA_C;
grupo:          GRUPO LL_A compañero+ LL_C;
compañero:      COMPAÑERO LL_A nomyape github? LL_C;

tecnologias:    TECNOLOGIAS PA_A CONJPALYNUM PA_C;
merito:         MERITOS LL_A nombre descripcion LL_C;

horas:          HORAS LL_A NUM LL_C; 