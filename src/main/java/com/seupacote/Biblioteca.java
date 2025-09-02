package com.seupacote;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Biblioteca {
    private List<Livro> livros;
    private static final String NOME_ARQUIVO = "livros.json";
    private Gson gson;

    public Biblioteca() {
        // GsonBuilder permite formatar o JSON para ficar legível
        this.gson = new GsonBuilder().setPrettyPrinting().create();
        this.livros = carregarLivros();
    }

    private ArrayList<Livro> carregarLivros() {
        try (FileReader reader = new FileReader(NOME_ARQUIVO)) {
            Type tipoListaLivros = new TypeToken<ArrayList<Livro>>() {}.getType();
            ArrayList<Livro> livrosCarregados = gson.fromJson(reader, tipoListaLivros);
            return livrosCarregados != null ? livrosCarregados : new ArrayList<>();
        } catch (IOException e) {
            // Se o arquivo não existe, retorna uma lista vazia
            return new ArrayList<>();
        }
    }

    public void salvarLivros() {
        try (FileWriter writer = new FileWriter(NOME_ARQUIVO)) {
            gson.toJson(livros, writer);
        } catch (IOException e) {
            System.err.println("Erro ao salvar os livros no arquivo: " + e.getMessage());
        }
    }

    public void adicionarLivro(Livro livro) {
        this.livros.add(livro);
        salvarLivros();
    }

    public void excluirLivro(int indice) {
        if (indice >= 0 && indice < livros.size()) {
            System.out.println("Livro \"" + livros.get(indice).getNome() + "\" excluído com sucesso!");
            this.livros.remove(indice);
            salvarLivros();
        } else {
            System.out.println("Índice inválido!");
        }
    }

    public List<Livro> getLivros() {
        return this.livros;
    }

    // Métodos de estatísticas
    public long contarLivrosPorSituacao(String situacao) {
        return livros.stream()
                     .filter(livro -> livro.getSituacao().equalsIgnoreCase(situacao))
                     .count();
    }

    public int paginometro() {
        return livros.stream()
                     .filter(livro -> livro.getSituacao().equalsIgnoreCase("Lido"))
                     .mapToInt(Livro::getPaginas)
                     .sum();
    }

    public double mediaPaginas() {
        List<Livro> livrosConsiderados = livros.stream()
            .filter(livro -> livro.getSituacao().equalsIgnoreCase("Lido") || livro.getSituacao().equalsIgnoreCase("Lendo"))
            .collect(Collectors.toList());

        if (livrosConsiderados.isEmpty()) {
            return 0.0;
        }

        int totalPaginas = livrosConsiderados.stream().mapToInt(Livro::getPaginas).sum();
        return (double) totalPaginas / livrosConsiderados.size();
    }

    public void mostrarLivrosPorAno() {
        Map<Integer, Long> livrosPorAno = livros.stream()
            .filter(livro -> livro.getSituacao().equalsIgnoreCase("Lido"))
            .collect(Collectors.groupingBy(Livro::getAno, Collectors.counting()));
        
        livrosPorAno.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(entry -> System.out.printf("- %d = %dx\n", entry.getKey(), entry.getValue()));
    }
}