package com.seupacote;

import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {
    private static Biblioteca biblioteca = new Biblioteca();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            exibirMenuPrincipal();
            try {
                int opcao = scanner.nextInt();
                scanner.nextLine(); // Consome a nova linha

                switch (opcao) {
                    case 1:
                        cadastrarLivro();
                        break;
                    case 2:
                        menuListarLivros();
                        break;
                    case 3:
                        excluirLivro();
                        break;
                    case 4:
                        exibirEstatisticas();
                        break;
                    case 5:
                        editarLivro();
                        break;
                    case 6:
                        System.out.println("Saindo do programa...");
                        biblioteca.salvarLivros(); // Garante que tudo foi salvo antes de sair
                        return;
                    default:
                        System.out.println("Opção inválida! Tente novamente.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Erro! Por favor, digite um número correspondente à opção.");
                scanner.nextLine(); // Limpa o buffer do scanner
            }
        }
    }
    
    // MÉTODOS DE INTERFACE COM O USUÁRIO

    private static void exibirMenuPrincipal() {
        cabecalho("Sistema de Controle de Leitura");
        System.out.println("1 - Cadastrar Livro");
        System.out.println("2 - Listar Livros");
        System.out.println("3 - Excluir Livro");
        System.out.println("4 - Estatísticas");
        System.out.println("5 - Editar Livro");
        System.out.println("6 - Sair do Programa");
        System.out.print("Sua opção: ");
    }

    private static void cadastrarLivro() {
        cabecalho("Cadastro de Livro");
        System.out.print("Nome do livro: ");
        String nome = scanner.nextLine();
        System.out.print("Nome do Autor(a): ");
        String autor = scanner.nextLine();

        String situacao = "";
        while (true) {
            System.out.println("--- Situação ---\n1 - Quero Ler\n2 - Lendo\n3 - Lido");
            System.out.print("Sua opção: ");
            int opSituacao = scanner.nextInt();
            scanner.nextLine();
            if (opSituacao == 1) { situacao = "Quero Ler"; break; }
            if (opSituacao == 2) { situacao = "Lendo"; break; }
            if (opSituacao == 3) { situacao = "Lido"; break; }
            System.out.println("Erro! Selecione uma opção válida.");
        }

        System.out.print("Ano de leitura: ");
        int ano = scanner.nextInt();
        System.out.print("Páginas: ");
        int paginas = scanner.nextInt();
        scanner.nextLine(); // Consome a nova linha

        Livro novoLivro = new Livro(nome, autor, situacao, ano, paginas);
        biblioteca.adicionarLivro(novoLivro);
        System.out.println("Livro cadastrado com sucesso!");
    }

    private static void menuListarLivros() {
        while (true) {
            cabecalho("Listagem de Livros");
            System.out.println("1 - Lendo\n2 - Quero Ler\n3 - Lido\n4 - Abandonados\n5 - Voltar");
            System.out.print("Sua opção: ");
            try {
                int subOpcao = scanner.nextInt();
                scanner.nextLine();
                if (subOpcao == 5) break;
                
                String situacao = "";
                switch (subOpcao) {
                    case 1: situacao = "Lendo"; break;
                    case 2: situacao = "Quero Ler"; break;
                    case 3: situacao = "Lido"; break;
                    case 4: situacao = "Abandonado"; break;
                    default: System.out.println("Opção inválida!"); continue;
                }
                listarLivros(situacao);
            } catch (InputMismatchException e) {
                System.out.println("Erro! Digite um número.");
                scanner.nextLine();
            }
        }
    }
    
    private static void listarLivros(String situacaoFiltro) {
        List<Livro> todosLivros = biblioteca.getLivros();
        if (todosLivros.isEmpty()) {
            System.out.println("Nenhum livro cadastrado!");
            return;
        }
        
        cabecalho("Livros com status: " + situacaoFiltro);
        System.out.printf("%-5s %-25s %-20s %-12s %-5s %-5s\n", "Nº", "Nome", "Autor(a)", "Situação", "Ano", "NP");
        System.out.println(new String(new char[75]).replace("\0", "-"));
        
        AtomicInteger count = new AtomicInteger(0);
        todosLivros.stream()
            .filter(livro -> situacaoFiltro.isEmpty() || livro.getSituacao().equalsIgnoreCase(situacaoFiltro))
            .forEach(livro -> {
                System.out.printf("%-5d %-25s %-20s %-12s %-5d %-5d\n",
                    (todosLivros.indexOf(livro) + 1), // Nº original na lista completa
                    limitarTexto(livro.getNome(), 25),
                    limitarTexto(livro.getAutor(), 20),
                    limitarTexto(livro.getSituacao(), 12),
                    livro.getAno(),
                    livro.getPaginas());
                count.incrementAndGet();
            });
            
        System.out.println(new String(new char[75]).replace("\0", "-"));
        System.out.printf("*** Total de Livros nesta lista: %d ***\n", count.get());
    }

    private static void excluirLivro() {
        cabecalho("Excluir Livro");
        listarLivros(""); // Lista todos os livros para o usuário escolher
        System.out.print("Digite o Nº do livro a ser excluído (0 para voltar): ");
        try {
            int indice = scanner.nextInt();
            scanner.nextLine();
            if (indice == 0) return;
            biblioteca.excluirLivro(indice - 1); // Ajusta para o índice da lista (começa em 0)
        } catch (InputMismatchException e) {
            System.out.println("Erro! Digite um número válido.");
            scanner.nextLine();
        }
    }

    private static void editarLivro() {
        cabecalho("Editar Livro");
        listarLivros(""); // Lista todos os livros
        System.out.print("Digite o Nº do livro para editar: ");
        try {
            int indice = scanner.nextInt() - 1; // Ajusta para o índice 0
            scanner.nextLine();

            if (indice < 0 || indice >= biblioteca.getLivros().size()) {
                System.out.println("Livro não encontrado!");
                return;
            }

            Livro livro = biblioteca.getLivros().get(indice);
            System.out.println("Editando: " + livro.getNome());
            System.out.println("1 - Editar Situação\n2 - Editar Ano\n3 - Editar Nº de Páginas");
            System.out.print("Sua opção: ");
            int opEditar = scanner.nextInt();
            scanner.nextLine();

            switch (opEditar) {
                case 1:
                    System.out.print("Nova situação [Quero Ler, Lido, Lendo, Abandonado]: ");
                    livro.setSituacao(scanner.nextLine());
                    break;
                case 2:
                    System.out.print("Novo ano: ");
                    livro.setAno(scanner.nextInt());
                    scanner.nextLine();
                    break;
                case 3:
                    System.out.print("Novo Nº de páginas: ");
                    livro.setPaginas(scanner.nextInt());
                    scanner.nextLine();
                    break;
                default:
                    System.out.println("Opção inválida. Nenhuma alteração feita.");
                    return;
            }
            biblioteca.salvarLivros();
            System.out.println("Alteração realizada com sucesso!");

        } catch (InputMismatchException e) {
            System.out.println("Erro! Digite um número válido.");
            scanner.nextLine();
        }
    }
    
    private static void exibirEstatisticas() {
        cabecalho("Estatísticas de Leitura");
        biblioteca.mostrarLivrosPorAno();
        System.out.printf("- Abandonados = %dx\n", biblioteca.contarLivrosPorSituacao("Abandonado"));
        System.out.printf("- Paginômetro (total de págs lidas) = %d\n", biblioteca.paginometro());
        System.out.printf("- Média de Páginas = %.2f\n", biblioteca.mediaPaginas());
    }

    // MÉTODOS UTILITÁRIOS (equivalentes às suas funções de formatação)
    
    private static void cabecalho(String msg) {
        String linha = new String(new char[60]).replace('\0', '-');
        System.out.println(linha);
        System.out.printf("%" + (30 + msg.length() / 2) + "s\n", msg);
        System.out.println(linha);
    }
    
    private static String limitarTexto(String texto, int limite) {
        if (texto.length() > limite) {
            return texto.substring(0, limite - 3) + "...";
        }
        return texto;
    }
}