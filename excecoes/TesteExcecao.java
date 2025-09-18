import java.util.*;

public class TesteExcecao {

      public String getCapital(String uf) throws Exception {
           Map<String, String> map = new HashMap<>();
           map.put("RS", "Porto Alegre");
           map.put("SP", "Sao Paulo");

           if (map.containsKey(uf)) {
                return map.get(uf);
           }
           else {
              throw new Exception("Chave nao existe no dicionario");
           }
      }

      public static void main(String args[]) {
        try {
           TesteExcecao te = new TesteExcecao();
           String uf = "RS";
           System.out.println(te.getCapital(uf));
        }
        catch(Exception e) {
            System.out.print(e.getMessage());
        }
      }

} 