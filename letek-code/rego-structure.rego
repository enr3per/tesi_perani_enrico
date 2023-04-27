package esempi_struttura

default allow := false

allow if {
    input.user == "Andrea"
    input.method == "GET"
}