/* ======== Analizador léxico JFlex corregido ======== */

%%

%class analizador
%standalone
%unicode
%line
%column

%state COMMENT

/* ======== Macros (expresiones regulares) ======== */

NUM               = (0|[1-9][0-9]*)
PAL               = ([A-Z]|[a-z]|[ÁÉÍÓÚáéíóúÑñ])+
MAIL              = ([A-Z]|[a-z]|[0-9])+ (.([A-Z]|[a-z]|[0-9]))* "@" ([A-Z]|[a-z]|[0-9])+ (.([A-Z]|[a-z]|[0-9]))*
RUTA              = ([A-Z]|[a-z])+ ("/"|"."|"-"|":")+ ([A-Z]|[a-z])+ (("/"|"."|"-"|":")+ ([A-Z]|[a-z])+)+ 
DIA               = (0[1-9]|(1|2)[0-9]|30|31)
MES               = (0[1-9]|1[0-2])
AÑO               = (1|2)[0-9][0-9][0-9]
BOOL              = (Si|No)
NVI               = (([ABC][12])|nativo)
NVH               = (bajo|medio|alto)
CE                = ("!"|"\""|"#"|"$"|"%"|"&"|"'"|"("|")"|"*"|"+"|","|"\\"|"-"|"."|"/"|":"|";"|"<"|"="|">"|"?"|"@"|"["|"]"|"^"|"‘"|"{"|"|"|"}"|"~"|"_") 
IDENT             = ([A-Z]|[a-z])([A-Z]|[a-z]|[0-9])*

%%

/* ================================================== */
/* ==================   REGLAS   ==================== */
/* ================================================== */

/* ======== Comentarios estilo C ======== */
<COMMENT> "*/"                   { yybegin(YYINITIAL); }
<COMMENT> <<EOF>>                { System.err.println("Error léxico en la línea " + (yyline+1) + ", columna " + (yycolumn+1) + ": Fin de archivo dentro de comentario."); System.exit(1); }
<COMMENT> .                      {} /* ignorar contenido del comentario */

/* ======== Palabras clave ======== */
<YYINITIAL>"cv"                  { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"id"                  { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"gvar"                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"lvar"                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"datospersonales"     { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"nomyape"             { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"foto"                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"fecha"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"bio"                 { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"contacto"            { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"email"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"telefono"            { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"redes"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"linkedin"            { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"github"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"web"                 { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"formacion"           { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"oficial"             { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"titulo"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"expedidor"           { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"descripcion"         { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"logros"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"complementaria"      { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"certificado"         { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"horas"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"idiomas"             { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"idioma"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"nivel"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"experiencia"         { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"laboral"             { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"puesto"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"responsabilidades"   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"voluntariado"        { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"organizacion"        { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"habilidades"         { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"soft"                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"hard"                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"habilidad"           { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"categoria"           { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

<YYINITIAL>"portafolio"          { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"proyecto"            { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"nombre"              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"grupo"               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"compañero"           { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"tecnologias"         { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"meritos"             { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

/* ======== Simbolos y Operadores ======== */
<YYINITIAL>"/*"                  { yybegin(COMMENT); }

<YYINITIAL>"{"                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"}"                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"("                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>")"                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>"="                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>";"                   { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

/* ======== Macros como tokens ======== */
<YYINITIAL>{NVH}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{NVI}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{MAIL}               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{RUTA}               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{DIA}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{MES}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{AÑO}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{NUM}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{IDENT}              { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{BOOL}               { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{PAL}                { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }
<YYINITIAL>{CE}                 { System.out.println("Token: " + yytext() + " en fila: " + (yyline) + " en columna: " + (yycolumn)); }

/* ======== Espacios en blanco ======== */
[|\t|\r|\n|" "]+                {} /* ignorar */

/* ======== Error léxico ======== */
<YYINITIAL>.                    {System.err.println("Error léxico en la línea " + (yyline) + ", columna " + (yycolumn) + ": carácter inesperado '" + yytext() + "'"); System.exit(1); }
