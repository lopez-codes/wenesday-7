import pytest

from baselines.common.segment_tree import SumSegmentTree, MinSegmentTree


@pytest.fixture
def sum_tree():
    """Return a fresh SumSegmentTree with four elements."""
    return SumSegmentTree(4)


@pytest.fixture
def min_tree():
    """Return a fresh MinSegmentTree with four elements."""
    return MinSegmentTree(4)


def test_tree_set(sum_tree):
    tree = sum_tree

    tree[2] = 1.0
    tree[3] = 3.0

    assert tree.sum() == pytest.approx(4.0)
    assert tree.sum(0, 2) == pytest.approx(0.0)
    assert tree.sum(0, 3) == pytest.approx(1.0)
    assert tree.sum(2, 3) == pytest.approx(1.0)
    assert tree.sum(2, -1) == pytest.approx(1.0)
    assert tree.sum(2, 4) == pytest.approx(4.0)


def test_tree_set_overlap(sum_tree):
    tree = sum_tree

    tree[2] = 1.0
    tree[2] = 3.0

    assert tree.sum() == pytest.approx(3.0)
    assert tree.sum(2, 3) == pytest.approx(3.0)
    assert tree.sum(2, -1) == pytest.approx(3.0)
    assert tree.sum(2, 4) == pytest.approx(3.0)
    assert tree.sum(1, 2) == pytest.approx(0.0)


def test_prefixsum_idx(sum_tree):
    tree = sum_tree

    tree[2] = 1.0
    tree[3] = 3.0

    assert tree.find_prefixsum_idx(0.0) == 2
    assert tree.find_prefixsum_idx(0.5) == 2
    assert tree.find_prefixsum_idx(0.99) == 2
    assert tree.find_prefixsum_idx(1.01) == 3
    assert tree.find_prefixsum_idx(3.00) == 3
    assert tree.find_prefixsum_idx(4.00) == 3


def test_prefixsum_idx2(sum_tree):
    tree = sum_tree

    tree[0] = 0.5
    tree[1] = 1.0
    tree[2] = 1.0
    tree[3] = 3.0

    assert tree.find_prefixsum_idx(0.00) == 0
    assert tree.find_prefixsum_idx(0.55) == 1
    assert tree.find_prefixsum_idx(0.99) == 1
    assert tree.find_prefixsum_idx(1.51) == 2
    assert tree.find_prefixsum_idx(3.00) == 3
    assert tree.find_prefixsum_idx(5.50) == 3


def test_max_interval_tree(min_tree):
    tree = min_tree

    tree[0] = 1.0
    tree[2] = 0.5
    tree[3] = 3.0

    assert tree.min() == pytest.approx(0.5)
    assert tree.min(0, 2) == pytest.approx(1.0)
    assert tree.min(0, 3) == pytest.approx(0.5)
    assert tree.min(0, -1) == pytest.approx(0.5)
    assert tree.min(2, 4) == pytest.approx(0.5)
    assert tree.min(3, 4) == pytest.approx(3.0)

    tree[2] = 0.7

    assert tree.min() == pytest.approx(0.7)
    assert tree.min(0, 2) == pytest.approx(1.0)
    assert tree.min(0, 3) == pytest.approx(0.7)
    assert tree.min(0, -1) == pytest.approx(0.7)
    assert tree.min(2, 4) == pytest.approx(0.7)
    assert tree.min(3, 4) == pytest.approx(3.0)

    tree[2] = 4.0

    assert tree.min() == pytest.approx(1.0)
    assert tree.min(0, 2) == pytest.approx(1.0)
    assert tree.min(0, 3) == pytest.approx(1.0)
    assert tree.min(0, -1) == pytest.approx(1.0)
    assert tree.min(2, 4) == pytest.approx(3.0)
    assert tree.min(2, 3) == pytest.approx(4.0)
    assert tree.min(2, -1) == pytest.approx(4.0)
    assert tree.min(3, 4) == pytest.approx(3.0)

