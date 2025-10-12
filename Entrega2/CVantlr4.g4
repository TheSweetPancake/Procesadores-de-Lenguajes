lexer grammar CVantlr4;

// ======== Palabras clave ========
CV              : 'cv' ;
ID              : 'id' ;
GVAR            : 'gvar' ;
LVAR            : 'lvar' ;

DATOS_PERSONALES: 'datospersonales' ;
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

// ======== Comentarios estilo C ========

COMMENT
    : '/*' .*? '*/' -> skip
    ;

// ======== Macros ========
NUM             : ('0' | [1-9][0-9]*) ;
PAL             : [A-Za-zÁÉÍÓÚáéíóúÑñ]+ ;
IDENT           : ([A-Z]|[a-z])([A-Z]|[a-z]|[0-9])* ;
MAIL            : [A-Za-z0-9]+ ('.' [A-Za-z0-9]+)* '@' [A-Za-z0-9]+ ('.' [A-Za-z0-9]+)* ;
RUTA            : [A-Za-z]+ ( [./\-:]+ [A-Za-z]+ )+ ;
DIA             : '0'[1-9] | [12][0-9] | '30' | '31' ;
MES             : '0'[1-9] | '1'[0-2] ;
AÑO             : [12][0-9][0-9][0-9] ;
BOOL            : 'Si' | 'No' ;
NVI             : ([ABC][12]) | 'nativo' ;
NVH             : 'bajo' | 'medio' | 'alto' ;
CE              : [!"#$%&'()+,\-.:;<=>?@[\\\]^_‘{|}~] ;

// ======== Espacios y saltos de línea ========
WS              : [ \t\r\n]+ -> skip ;

// ======== Manejo de errores ========
ERROR       : . ;
