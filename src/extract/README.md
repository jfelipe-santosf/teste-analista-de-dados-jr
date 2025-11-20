## Extração dos dados

Por se tratar de algo simples como um db local procurei usar `métodos simples` para extrair os dados porém `redudantes`.

### Consulta

```sql
SELECT
    c.id_cliente,
    v.id_venda,
    c.nome,
    c.email,
    c.estado,
    c.segmento,
    v.data_venda,
    v.quantidade,
    v.preco_unitario,
    v.desconto_percentual
FROM clientes c
JOIN vendas v
    ON c.id_cliente = v.id_cliente
```
Um simples join para crusar id_cliente entre as duas tabelas.

