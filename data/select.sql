SELECT
    c.id_cliente,
    v.id_venda,
    c.nome AS nome,
    c.email AS email,
    c.estado AS estado,
    c.segmento AS segmento,
    v.data_venda,
    v.quantidade,
    v.preco_unitario,
    v.desconto_percentual
FROM clientes c
JOIN vendas v
    ON c.id_cliente = v.id_cliente