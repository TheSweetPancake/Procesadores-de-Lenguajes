/* ======== Analizador léxico JFlex corregido ======== */

%%

%class analizador
%standalone
%unicode
%line
%column

%cup

%state COMMENT

/* ======== Macros (expresiones regulares) ======== */

NUM               = (0|[1-9][0-9]*)
PAL               = ([A-Z]|[a-z]|[ÁÉÍÓÚáéíóúÑñ])+
TFNO              = ([5-9][0-9]{8})
MAIL              = ([A-Z]|[a-z]|[0-9])+(\.[A-Z]|[a-z]|[0-9]+)*"@"([A-Z]|[a-z]|[0-9])+(\.[A-Z]|[a-z]|[0-9]+)*
RUTA              = ([A-Z]|[a-z])+ ("/"|"."|"-"|":")+ ([A-Z]|[a-z])+ (("/"|"."|"-"|":")+ ([A-Z]|[a-z])+)+ 
DIA               = (0[1-9]|(1|2)[0-9]|30|31)
MES               = (0[1-9]|1[0-2])
ANIO              = (1|2)[0-9][0-9][0-9]
BOOL              = (Si|No)
NVI               = (([ABC][12])|nativo)
NVH               = (bajo|medio|alto)
IDENT             = ([A-Z]|[a-z])([A-Z]|[a-z]|[0-9])*
CONJPAL           = {PAL}(\s+{PAL})*
CONJPALYNUM       = {PAL}(\s+{PAL}|\s+{NUM})*

%%

/* ================================================== */
/* ==================   REGLAS   ==================== */
/* ================================================== */

/* ======== Comentarios estilo C ======== */
<COMMENT> "*/"                   { yybegin(YYINITIAL); }
<COMMENT> <<EOF>>                { System.err.println("Error léxico en la línea " + (yyline+1) + ", columna " + (yycolumn+1) + ": Fin de archivo dentro de comentario."); System.exit(1); }
<COMMENT> .                      {} /* ignorar contenido del comentario */

/* ======== Palabras clave ======== */
<YYINITIAL>"cv"                  { return new Symbol(sym.cv); }
<YYINITIAL>"id"                  { return new Symbol(sym.id); }
<YYINITIAL>"gvar"                { return new Symbol(sym.gvar); }
<YYINITIAL>"lvar"                { return new Symbol(sym.lvar); }

<YYINITIAL>"datospersonales"     { return new Symbol(sym.datospersonales); }
<YYINITIAL>"nomyape"             { return new Symbol(sym.nomyape); }
<YYINITIAL>"foto"                { return new Symbol(sym.foto); }
<YYINITIAL>"fecha"               { return new Symbol(sym.fecha); }
<YYINITIAL>"bio"                 { return new Symbol(sym.bio); }
<YYINITIAL>"contacto"            { return new Symbol(sym.contacto); }
<YYINITIAL>"email"               { return new Symbol(sym.email); }
<YYINITIAL>"telefono"            { return new Symbol(sym.telefono); }
<YYINITIAL>"redes"               { return new Symbol(sym.redes); }
<YYINITIAL>"linkedin"            { return new Symbol(sym.linkedin); }
<YYINITIAL>"github"              { return new Symbol(sym.github); }
<YYINITIAL>"web"                 { return new Symbol(sym.web); }

<YYINITIAL>"formacion"           { return new Symbol(sym.formacion); }
<YYINITIAL>"oficial"             { return new Symbol(sym.oficial); }
<YYINITIAL>"titulo"              { return new Symbol(sym.titulo); }
<YYINITIAL>"expedidor"           { return new Symbol(sym.expedidor); }
<YYINITIAL>"descripcion"         { return new Symbol(sym.descripcion); }
<YYINITIAL>"logros"              { return new Symbol(sym.logros); }
<YYINITIAL>"complementaria"      { return new Symbol(sym.complementaria); }
<YYINITIAL>"certificado"         { return new Symbol(sym.certificado); }
<YYINITIAL>"horas"               { return new Symbol(sym.horas); }

<YYINITIAL>"idiomas"             { return new Symbol(sym.idiomas); }
<YYINITIAL>"idioma"              { return new Symbol(sym.idioma); }
<YYINITIAL>"nivel"               { return new Symbol(sym.nivel); }

<YYINITIAL>"experiencia"         { return new Symbol(sym.experiencia); }
<YYINITIAL>"laboral"             { return new Symbol(sym.laboral); }
<YYINITIAL>"puesto"              { return new Symbol(sym.puesto); }
<YYINITIAL>"responsabilidades"   { return new Symbol(sym.responsabilidades); }
<YYINITIAL>"voluntariado"        { return new Symbol(sym.voluntariado); }
<YYINITIAL>"organizacion"        { return new Symbol(sym.organizacion); }

<YYINITIAL>"habilidades"         { return new Symbol(sym.habilidades); }
<YYINITIAL>"soft"                { return new Symbol(sym.soft); }
<YYINITIAL>"hard"                { return new Symbol(sym.hard); }
<YYINITIAL>"nvhab"               { return new Symbol(sym.nvhab); }
<YYINITIAL>"habilidad"           { return new Symbol(sym.habilidad); }
<YYINITIAL>"categoria"           { return new Symbol(sym.categoria); }

<YYINITIAL>"portafolio"          { return new Symbol(sym.portafolio); }
<YYINITIAL>"proyecto"            { return new Symbol(sym.proyecto); }
<YYINITIAL>"nombre"              { return new Symbol(sym.nombre); }
<YYINITIAL>"grupo"               { return new Symbol(sym.grupo); }
<YYINITIAL>"compañero"           { return new Symbol(sym.compañero); }
<YYINITIAL>"tecnologias"         { return new Symbol(sym.tecnologias); }
<YYINITIAL>"meritos"             { return new Symbol(sym.meritos); }

/* ======== Símbolos y operadores ======== */
<YYINITIAL>"/*"                  { yybegin(COMMENT); }

<YYINITIAL>"{"                   { return new Symbol(sym.LLAVE_ABRE); }
<YYINITIAL>"}"                   { return new Symbol(sym.LLAVE_CIERRA); }
<YYINITIAL>"("                   { return new Symbol(sym.PAR_ABRE); }
<YYINITIAL>")"                   { return new Symbol(sym.PAR_CIERRA); }
<YYINITIAL>","                   { return new Symbol(sym.CO); }
<YYINITIAL>"\""                  { return new Symbol(sym.CD); }
<YYINITIAL>"="                   { return new Symbol(sym.IGUAL); }
<YYINITIAL>";"                   { return new Symbol(sym.PYC); }

/* ======== Macros ======== */
<YYINITIAL>{BOOL}                { return new Symbol(sym.BOOL); }
<YYINITIAL>{NVH}                 { return new Symbol(sym.NVH); }
<YYINITIAL>{NVI}                 { return new Symbol(sym.NVI); }
<YYINITIAL>{MAIL}                { return new Symbol(sym.MAIL); }
<YYINITIAL>{RUTA}                { return new Symbol(sym.RUTA); }
<YYINITIAL>{TFNO}                { return new Symbol(sym.TFNO); }
<YYINITIAL>{MES}                 { return new Symbol(sym.MES); }
<YYINITIAL>{DIA}                 { return new Symbol(sym.DIA); }
<YYINITIAL>{ANIO}                { return new Symbol(sym.ANIO); }
<YYINITIAL>{NUM}                 { return new Symbol(sym.NUM); }
<YYINITIAL>{IDENT}               { return new Symbol(sym.IDENT); }
<YYINITIAL>{PAL}                 { return new Symbol(sym.PAL); }
<YYINITIAL>{CONJPAL}             { return new Symbol(sym.CONJPAL); }
<YYINITIAL>{CONJPALYNUM}         { return new Symbol(sym.CONJPALYNUM); }

/* ======== Espacios en blanco ======== */
[|\t|\r|\n|" "]+                {} /* ignorar */

/* ======== Error léxico ======== */
<YYINITIAL>.                    {System.err.println("Error léxico en la línea " + (yyline) + ", columna " + (yycolumn) + ": carácter inesperado '" + yytext() + "'"); System.exit(1); }
