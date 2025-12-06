from tp5 import *
import time


def create_test_matrices():
    """Create various test matrices for different scenarios"""

    # Test Case 1: Simple 3x3 system
    A1 = [
        [4.0, -1.0, 0.0],
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 4.0]
    ]
    b1 = [15.0, 10.0, 10.0]
    B1 = [
        [2.0, 1.0, 0.0],
        [1.0, 2.0, 1.0],
        [0.0, 1.0, 2.0]
    ]

    # Test Case 2: Triangular matrices
    A2_upper = [
        [2.0, 3.0, 1.0],
        [0.0, 4.0, 2.0],
        [0.0, 0.0, 5.0]
    ]
    b2 = [11.0, 10.0, 15.0]

    A2_lower = [
        [3.0, 0.0, 0.0],
        [2.0, 4.0, 0.0],
        [1.0, 3.0, 5.0]
    ]

    # Test Case 3: Diagonally dominant (good for iterative methods)
    A3 = [
        [10.0, -1.0, 2.0],
        [-1.0, 11.0, -1.0],
        [2.0, -1.0, 10.0]
    ]
    b3 = [6.0, 25.0, -11.0]

    # Test Case 4: Symmetric matrix
    A4 = [
        [4.0, 1.0, 2.0],
        [1.0, 3.0, 1.0],
        [2.0, 1.0, 5.0]
    ]
    b4 = [7.0, 5.0, 8.0]

    return {
        'simple': (A1, b1, B1),
        'triangular': (A2_upper, b2, A2_lower),
        'diagonal_dominant': (A3, b3, None),
        'symmetric': (A4, b4, None)
    }


def test_tp1_operations():
    """Test TP1: Basic matrix operations"""
    print("=" * 80)
    print("TESTING TP1: BASIC MATRIX OPERATIONS")
    print("=" * 80)

    test_cases = create_test_matrices()
    A, b, B = test_cases['simple']

    try:
        # Test 1: Display matrices
        print("\n--- Test 1: Display Matrices ---")
        print("Matrix A:")
        print_system(A)
        print("Matrix B:")
        print_system(B)

        # Test 2: Identity matrix
        print("\n--- Test 2: Identity Matrix ---")
        I = matriceDidentit(3)
        print("Identity matrix 3x3:")
        print_system(I)

        # Test 3: Matrix sum
        print("\n--- Test 3: Matrix Sum A + B ---")
        C = somme2matrices(A, B)
        print_system(C)

        # Test 4: Matrix product
        print("\n--- Test 4: Matrix Product A * B ---")
        P = produit2matrices(A, B)
        print_system(P)

        # Test 5: Transpose
        print("\n--- Test 5: Transpose of A ---")
        AT = transpose(A)
        print_system(AT)

        # Test 6: Check triangular upper
        print("\n--- Test 6: Triangular Tests ---")
        A_upper, _, A_lower = test_cases['triangular']
        print(f"Upper triangular matrix is upper triangular: {isTriangulaireSuprieure(A_upper)}")
        print(f"Lower triangular matrix is lower triangular: {isTriangulaireInfrieure(A_lower)}")

        # Test 7: Check diagonal
        print("\n--- Test 7: Diagonal Test ---")
        D = [[5.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 7.0]]
        print(f"Diagonal matrix is diagonal: {isDiagonale(D)}")

        # Test 8: Check symmetric
        print("\n--- Test 8: Symmetric Test ---")
        A_sym, _, _ = test_cases['symmetric']
        print(f"Symmetric matrix is symmetric: {isSymétrique(A_sym)}")

        # Test 9: Permutation
        print("\n--- Test 9: Row Permutation ---")
        A_copy = copier_matrice(A)
        permet2liner(A_copy, 0, 2)
        print("After swapping rows 0 and 2:")
        print_system(A_copy)

        # Test 10: Column permutation
        print("\n--- Test 10: Column Permutation ---")
        A_copy = copier_matrice(A)
        permet2col(A_copy, 0, 2)
        print("After swapping columns 0 and 2:")
        print_system(A_copy)

        # Test 11: Determinant
        print("\n--- Test 11: Determinant ---")
        det_iter = determinantIterative(A)
        det_rec = determinant(A)
        print(f"Determinant (iterative): {det_iter:.6f}")
        print(f"Determinant (recursive): {det_rec:.6f}")

        print("\n✓ TP1 Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ TP1 Test Failed: {e}")
        return False


def test_tp2_cramer():
    """Test TP2: Cramer's rule and substitution methods"""
    print("\n" + "=" * 80)
    print("TESTING TP2: CRAMER AND SUBSTITUTION METHODS")
    print("=" * 80)

    test_cases = create_test_matrices()

    try:
        # Test descent with lower triangular
        print("\n--- Test 1: Descent (Lower Triangular) ---")
        _, _, A_lower = test_cases['triangular']
        b_lower = [6.0, 14.0, 29.0]
        print("System:")
        print_system(A_lower, b_lower)
        x_desc_iter = descenteITR(copier_matrice(A_lower), b_lower[:])
        print("Solution (iterative):")
        printX(x_desc_iter)

        x_desc_rec = descenteREC(copier_matrice(A_lower), b_lower[:])
        print("Solution (recursive):")
        printX(x_desc_rec)

        # Test remontée with upper triangular
        print("\n--- Test 2: Remontée (Upper Triangular) ---")
        A_upper, b_upper, _ = test_cases['triangular']
        print("System:")
        print_system(A_upper, b_upper)
        x_rem_iter = remontéeITR(copier_matrice(A_upper), b_upper[:])
        print("Solution (iterative):")
        printX(x_rem_iter)

        x_rem_rec = remontéeREC(copier_matrice(A_upper), b_upper[:])
        print("Solution (recursive):")
        printX(x_rem_rec)

        # Test Cramer
        print("\n--- Test 3: Cramer's Rule ---")
        A, b, _ = test_cases['simple']
        print("System:")
        print_system(A, b)

        x_cramer_iter = Cramer(copier_matrice(A), b[:])
        print("Solution (iterative):")
        printX(x_cramer_iter)

        x_cramer_rec = RECramer(copier_matrice(A), b[:])
        print("Solution (recursive):")
        printX(x_cramer_rec)

        print("\n✓ TP2 Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ TP2 Test Failed: {e}")
        return False


def test_tp3_gauss():
    """Test TP3: Gauss elimination methods"""
    print("\n" + "=" * 80)
    print("TESTING TP3: GAUSS ELIMINATION METHODS")
    print("=" * 80)

    test_cases = create_test_matrices()
    A, b, _ = test_cases['simple']

    try:
        # Test 1: Normal Gauss (iterative)
        print("\n--- Test 1: Normal Gauss Elimination (Iterative) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri = triangularisation(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)

        # Test 2: Normal Gauss (recursive)
        print("\n--- Test 2: Normal Gauss Elimination (Recursive) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri = triangularisationREC(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)

        # Test 3: Partial pivot (iterative)
        print("\n--- Test 3: Gauss with Partial Pivot (Iterative) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri = triangularisationPP(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)

        # Test 4: Partial pivot (recursive)
        print("\n--- Test 4: Gauss with Partial Pivot (Recursive) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri = triangularisationPPREC(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)

        # Test 5: Total pivot (iterative)
        print("\n--- Test 5: Gauss with Total Pivot (Iterative) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri, col_perm = triangularisationPL(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)
        x_ordered = reorder_x_after_column_swaps(x, col_perm)

        # Test 6: Total pivot (recursive)
        print("\n--- Test 6: Gauss with Total Pivot (Recursive) ---")
        A_copy = copier_matrice(A)
        b_copy = b[:]
        A_tri, b_tri, col_perm = triangularisationPLREC(A_copy, b_copy)
        x = remontéeITR(A_tri, b_tri)
        x_ordered = reorder_x_after_column_swaps(x, col_perm)

        print("\n✓ TP3 Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ TP3 Test Failed: {e}")
        return False


def test_tp4_decomposition():
    """Test TP4: LU Decomposition and Gauss-Jordan"""
    print("\n" + "=" * 80)
    print("TESTING TP4: LU DECOMPOSITION AND GAUSS-JORDAN")
    print("=" * 80)

    test_cases = create_test_matrices()
    A, b, _ = test_cases['simple']

    try:
        # Test 1: LU Decomposition (iterative)
        print("\n--- Test 1: LU Decomposition (Iterative) ---")
        x = solve_LU(copier_matrice(A), b[:])

        # Test 2: LU Decomposition (recursive)
        print("\n--- Test 2: LU Decomposition (Recursive) ---")
        x = solve_LU_REC(copier_matrice(A), b[:])

        # Test 3: Gauss-Jordan solution (iterative)
        print("\n--- Test 3: Gauss-Jordan Solution (Iterative) ---")
        x = gauss_jordan_solution(copier_matrice(A), b[:])

        # Test 4: Gauss-Jordan inverse (iterative)
        print("\n--- Test 4: Gauss-Jordan Inverse (Iterative) ---")
        A_inv = gauss_jordan_inverse(copier_matrice(A))

        # Test 5: Gauss-Jordan solution (recursive)
        print("\n--- Test 5: Gauss-Jordan Solution (Recursive) ---")
        x = gauss_jordan_solution_REC(copier_matrice(A), b[:])

        # Test 6: Gauss-Jordan inverse (recursive)
        print("\n--- Test 6: Gauss-Jordan Inverse (Recursive) ---")
        A_inv = gauss_jordan_inverse_REC(copier_matrice(A))

        # Verify inverse by multiplying A * A_inv
        print("\n--- Verification: A * A^-1 should equal I ---")
        result = produit2matrices(A, A_inv)
        print_system(result)

        print("\n✓ TP4 Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ TP4 Test Failed: {e}")
        return False


def test_tp5_iterative():
    """Test TP5: Iterative methods (Jacobi and Gauss-Seidel)"""
    print("\n" + "=" * 80)
    print("TESTING TP5: ITERATIVE METHODS")
    print("=" * 80)

    test_cases = create_test_matrices()
    A, b, _ = test_cases['diagonal_dominant']

    n_max = 20
    epsilon = 1e-6

    try:
        # Test 1: Jacobi (iterative)
        print("\n--- Test 1: Jacobi Method (Iterative) ---")
        x = jacobi(copier_matrice(A), b[:], n_max, epsilon)

        # Test 2: Gauss-Seidel (iterative)
        print("\n--- Test 2: Gauss-Seidel Method (Iterative) ---")
        x = gauss_seidel(copier_matrice(A), b[:], n_max, epsilon)

        # Test 3: Jacobi (recursive)
        print("\n--- Test 3: Jacobi Method (Recursive) ---")
        x = jacobi_REC(copier_matrice(A), b[:], n_max, epsilon)

        # Test 4: Gauss-Seidel (recursive)
        print("\n--- Test 4: Gauss-Seidel Method (Recursive) ---")
        x = gauss_seidel_REC(copier_matrice(A), b[:], n_max, epsilon)

        # Test with non-diagonally dominant matrix (should show warning)
        print("\n--- Test 5: Non-Diagonally Dominant Matrix (Should Warn) ---")
        A_bad, b_bad, _ = test_cases['simple']
        x = jacobi(copier_matrice(A_bad), b_bad[:], 10, epsilon)

        print("\n✓ TP5 Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ TP5 Test Failed: {e}")
        return False


def test_edge_cases():
    """Test edge cases and special scenarios"""
    print("\n" + "=" * 80)
    print("TESTING EDGE CASES")
    print("=" * 80)

    try:
        # Test 1: 2x2 system
        print("\n--- Test 1: Small 2x2 System ---")
        A_small = [[3.0, 2.0], [1.0, 4.0]]
        b_small = [7.0, 6.0]
        print("System:")
        print_system(A_small, b_small)
        x = Cramer(A_small, b_small)
        print("Solution:")
        printX(x)

        # Test 2: Singular matrix (should fail gracefully)
        print("\n--- Test 2: Singular Matrix (det = 0) ---")
        A_singular = [[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [1.0, 1.0, 1.0]]
        b_singular = [1.0, 2.0, 3.0]
        print("System:")
        print_system(A_singular, b_singular)
        try:
            x = Cramer(A_singular, b_singular)
            if x is None:
                print("Correctly detected singular matrix (det = 0)")
        except:
            print("Correctly raised exception for singular matrix")

        # Test 3: 4x4 system
        print("\n--- Test 3: Larger 4x4 System ---")
        A_large = [
            [5.0, -1.0, 0.0, 0.0],
            [-1.0, 5.0, -1.0, 0.0],
            [0.0, -1.0, 5.0, -1.0],
            [0.0, 0.0, -1.0, 5.0]
        ]
        b_large = [4.0, 3.0, 2.0, 1.0]
        print("System:")
        print_system(A_large, b_large)
        x = solve_LU(copier_matrice(A_large), b_large[:])

        print("\n✓ Edge Cases Tests Completed Successfully")
        return True

    except Exception as e:
        print(f"\n✗ Edge Cases Test Failed: {e}")
        return False


def run_all_tests():
    """Run all test suites"""
    print("\n")
    print("*" * 80)
    print("*" + " " * 78 + "*")
    print("*" + " " * 20 + "COMPREHENSIVE TEST SUITE" + " " * 33 + "*")
    print("*" + " " * 78 + "*")
    print("*" * 80)

    start_time = time.perf_counter()

    results = {
        'TP1 - Basic Operations': test_tp1_operations(),
        'TP2 - Cramer & Substitution': test_tp2_cramer(),
        'TP3 - Gauss Elimination': test_tp3_gauss(),
        'TP4 - LU & Gauss-Jordan': test_tp4_decomposition(),
        'TP5 - Iterative Methods': test_tp5_iterative(),
        'Edge Cases': test_edge_cases()
    }

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Print summary
    print("\n")
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    passed = sum(results.values())
    total = len(results)

    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name:.<50} {status}")

    print("=" * 80)
    print(f"Total: {passed}/{total} test suites passed")
    print(f"Execution time: {execution_time:.4f} seconds")
    print("=" * 80)

    if passed == total:
        print("\n🎉 ALL TESTS PASSED! 🎉")
    else:
        print(f"\n⚠️  {total - passed} test suite(s) failed")

    return results


def quick_test():
    """Quick test with minimal output for rapid verification"""
    print("\n" + "=" * 80)
    print("QUICK TEST - MINIMAL OUTPUT")
    print("=" * 80)

    test_cases = create_test_matrices()
    A, b, _ = test_cases['simple']

    try:
        # Test each major algorithm once
        print("\nTesting Cramer...", end=" ")
        x1 = Cramer(copier_matrice(A), b[:])
        print("✓")

        print("Testing Gauss elimination...", end=" ")
        A_copy, b_copy = triangularisation(copier_matrice(A), b[:])
        x2 = remontéeITR(A_copy, b_copy)
        print("✓")

        print("Testing LU decomposition...", end=" ")
        x3 = solve_LU(copier_matrice(A), b[:])
        print("✓")

        print("Testing Gauss-Jordan...", end=" ")
        x4 = gauss_jordan_solution(copier_matrice(A), b[:])
        print("✓")

        A_iter, b_iter, _ = test_cases['diagonal_dominant']
        print("Testing Jacobi...", end=" ")
        x5 = jacobi(copier_matrice(A_iter), b_iter[:], 20, 1e-6)
        print("✓")

        print("\n✓ All quick tests passed!")
        return True

    except Exception as e:
        print(f"\n✗ Quick test failed: {e}")
        return False


if __name__ == "__main__":
    print("\nChoose test mode:")
    print("1. Run all comprehensive tests")
    print("2. Run quick test (minimal output)")
    print("3. Test specific TP")

    choice = input("\nYour choice (1/2/3): ").strip()

    if choice == "1":
        run_all_tests()
    elif choice == "2":
        quick_test()
    elif choice == "3":
        print("\nWhich TP to test?")
        print("1. TP1 - Basic Operations")
        print("2. TP2 - Cramer & Substitution")
        print("3. TP3 - Gauss Elimination")
        print("4. TP4 - LU & Gauss-Jordan")
        print("5. TP5 - Iterative Methods")
        print("6. Edge Cases")

        tp_choice = input("\nYour choice (1-6): ").strip()

        if tp_choice == "1":
            test_tp1_operations()
        elif tp_choice == "2":
            test_tp2_cramer()
        elif tp_choice == "3":
            test_tp3_gauss()
        elif tp_choice == "4":
            test_tp4_decomposition()
        elif tp_choice == "5":
            test_tp5_iterative()
        elif tp_choice == "6":
            test_edge_cases()
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")