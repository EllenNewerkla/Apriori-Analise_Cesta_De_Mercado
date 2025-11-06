"""
Classe MBA com métodos personalizados para suporte, confiança e lift,
e função para gerar regras a partir de itemsets frequentes.
Assume que 'transactions' é uma lista de listas (cada compra é uma lista de itens).
"""

from itertools import combinations
from collections import Counter
from typing import List, Tuple, Dict, Set

class MBA:
    def __init__(self, transactions: List[List[str]]):
        """
        transactions: lista de compras, cada compra é lista de itens (strings).
        Converte itens para str normalizados (já espere que o notebook normalize).
        """
        self.transactions = [tuple(t) for t in transactions]
        self.n_transactions = len(self.transactions)
        # contador de ocorrências de itemsets de tamanho 1 (útil)
        all_items = [item for t in self.transactions for item in t]
        self.single_counts = Counter(all_items)
        # Cache para contagens de itemsets
        self._cache_counts = {}

    def _count_itemset(self, itemset: Tuple[str, ...]) -> int:
        """Conta quantas transações contêm todos os itens do itemset."""
        key = tuple(sorted(itemset))
        if key in self._cache_counts:
            return self._cache_counts[key]
        count = 0
        s = set(key)
        for t in self.transactions:
            if s.issubset(set(t)):
                count += 1
        self._cache_counts[key] = count
        return count

    def support(self, itemset: List[str]) -> float:
        """Retorna suporte do itemset (como proporção de transações)."""
        if len(itemset) == 0:
            return 0.0
        count = self._count_itemset(tuple(itemset))
        return count / self.n_transactions

    def confidence(self, antecedent: List[str], consequent: List[str]) -> float:
        """Conf(antecedent -> consequent) = sup(antecedent ∪ consequent) / sup(antecedent)."""
        if len(antecedent) == 0:
            return 0.0
        sup_ant = self.support(antecedent)
        if sup_ant == 0:
            return 0.0
        sup_union = self.support(list(set(antecedent) | set(consequent)))
        return sup_union / sup_ant

    def lift(self, antecedent: List[str], consequent: List[str]) -> float:
        """Lift = sup(A ∪ B) / (sup(A) * sup(B))"""
        sup_union = self.support(list(set(antecedent) | set(consequent)))
        sup_a = self.support(antecedent)
        sup_b = self.support(consequent)
        if sup_a == 0 or sup_b == 0:
            return 0.0
        return sup_union / (sup_a * sup_b)

    def generate_rules_from_frequent_itemsets(
        self,
        frequent_itemsets: List[Tuple[Tuple[str, ...], float]],
        min_confidence: float = 0.5,
        min_lift: float = 1.0
    ) -> List[Dict]:
        """
        Gera todas as regras (A -> B) a partir de frequent_itemsets.
        frequent_itemsets: lista de tuplas (itemset_tuple, support_value)
        Retorna lista de regras com suporte, confiança e lift.
        """
        rules = []
        # transformar para dicionário de suportes para lookup rápido
        support_dict = {tuple(sorted(list(itemset))): sup for itemset, sup in frequent_itemsets}

        for itemset, sup_itemset in frequent_itemsets:
            items = list(itemset)
            if len(items) < 2:
                continue
            # gerar todos os subconjuntos não vazios próprios como antecedente
            for r in range(1, len(items)):
                for antecedent in combinations(items, r):
                    consequent = tuple(sorted(set(items) - set(antecedent)))
                    antecedent = tuple(sorted(antecedent))
                    # calcular métricas via métodos (usa transactions para precisão)
                    sup_union = support_dict.get(tuple(sorted(items)), None)
                    # fallback se não tiver no dict (calcular)
                    if sup_union is None:
                        sup_union = self.support(list(items))
                    sup_ant = support_dict.get(tuple(sorted(antecedent)), None)
                    if sup_ant is None:
                        sup_ant = self.support(list(antecedent))
                    sup_cons = support_dict.get(tuple(sorted(consequent)), None)
                    if sup_cons is None:
                        sup_cons = self.support(list(consequent))

                    if sup_ant == 0:
                        continue
                    conf = sup_union / sup_ant
                    lift = 0.0
                    if sup_cons > 0:
                        lift = sup_union / (sup_ant * sup_cons)

                    if conf >= min_confidence and lift >= min_lift:
                        rules.append({
                            'antecedent': tuple(antecedent),
                            'consequent': tuple(consequent),
                            'support': sup_union,
                            'confidence': conf,
                            'lift': lift
                        })
        # ordenar por lift descendente (o enunciado pede por lift)
        rules_sorted = sorted(rules, key=lambda x: x['lift'], reverse=True)
        return rules_sorted
