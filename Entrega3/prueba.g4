grammar prueba;

s : ('a' s a)? ;     // S → 'a' S A | ε
a : c ;              // A → C
c : 'b' b? ;         // C → 'b' B | 'b'
b : (a 'c')? ;       // B → A 'c' | ε
