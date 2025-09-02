package com.seupacote;

public class Livro {
    private String nome;
    private String autor;
    private String situacao;
    private int ano;
    private int paginas;

    // Construtor
    public Livro(String nome, String autor, String situacao, int ano, int paginas) {
        this.nome = nome;
        this.autor = autor;
        this.situacao = situacao;
        this.ano = ano;
        this.paginas = paginas;
    }

    // Getters (para acessar os dados)
    public String getNome() { return nome; }
    public String getAutor() { return autor; }
    public String getSituacao() { return situacao; }
    public int getAno() { return ano; }
    public int getPaginas() { return paginas; }

    // Setters (para modificar os dados)
    public void setSituacao(String situacao) { this.situacao = situacao; }
    public void setAno(int ano) { this.ano = ano; }
    public void setPaginas(int paginas) { this.paginas = paginas; }
}