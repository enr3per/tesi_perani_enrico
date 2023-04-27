package accesso_dati 

default allow = false

allow {
    input.user.role == "manager"
}	# Questa regola consente ai manager di accedere a tutti i dati.

allow {
    input.user.role == "capo-area"
    not input.user.method == "DELETE"
    some i
    input.user.areas[i] == input.data.area

}	# Questa regola consente ai capiarea di accedere solo ai dati della loro area di competenza.

allow {
    input.user.role == "operaio"
    input.user.method == "GET"
  some i
    input.user.areas[i] == input.data.area
}	# Questa regola consente agli operai di accedere solo ai dati relativi alla loro area di competenza e in sola lettura.